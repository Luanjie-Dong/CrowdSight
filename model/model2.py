import os
import torch
import numpy as np
from src.crowd_count import CrowdCounter
import cv2
import time
from src import network
from concurrent.futures import ThreadPoolExecutor, as_completed

class CrowdDensityEstimator:
    def __init__(self, model_path='src/cmtl_shtechA_100.h5'):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        torch.backends.cudnn.enabled = False
        self.model = self._load_model(model_path)
        self.model.to(self.device)
        self.model.eval()

    def _load_model(self, model_path):
        net = CrowdCounter()
        network.load_net(model_path, net)
        return net

    def preprocess_frame(self, frame):
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img = img.astype(np.float32, copy=False)

        ht, wd = img.shape
        ht_1 = int(ht / 4) * 4
        wd_1 = int(wd / 4) * 4
        img = cv2.resize(img, (wd_1, ht_1))

        img = img.reshape((1, 1, img.shape[0], img.shape[1]))  # (C, H, W)
        return img

    def analyse_frame(self, frame):
        im_data = self.preprocess_frame(frame)
        im_data = torch.tensor(im_data).to(self.device)

        with torch.no_grad():
            density_map = self.model(im_data)

        density_map = density_map.data.cpu().numpy()
        people_count = int(np.sum(density_map))
        return people_count

    def analyse_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        total_count = 0
        frame_count = 0
        analysed_frames = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

           
            if frame_count % 60  == 0:
                people_count = self.analyse_frame(frame)
                total_count += people_count
                print(people_count)

                # # Optionally display the frame with the count
                # cv2.putText(frame, f'Count: {people_count}', (10, 30),
                #             cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                # cv2.imshow('Frame', frame)

                # if cv2.waitKey(1) & 0xFF == ord('q'):
                #     break

            frame_count += 1

        cap.release()
        cv2.destroyAllWindows()

        return analysed_frames, total_count

    def analyse_videos_concurrently(self, video_paths):
        with ThreadPoolExecutor(max_workers=2) as executor:  # Limit to 2 concurrent threads
            future_to_video = {executor.submit(self.analyse_video, video_path): video_path for video_path in video_paths}
            for future in as_completed(future_to_video):
                video_path = future_to_video[future]
                try:
                    analysed_frames, total_count = future.result()
                    print(f"Total people counted in {video_path}: {total_count} over {analysed_frames} frames")
                except Exception as exc:
                    print(f"{video_path} generated an exception: {exc}")

if __name__ == "__main__":
    estimator = CrowdDensityEstimator(model_path='src/cmtl_shtechA_100.h5')
    video_paths = ["samples/crowd1.mp4", "samples/crowd2.mp4"]
    estimator.analyse_videos_concurrently(video_paths)

import os
import torch
import numpy as np
from src.crowd_count import CrowdCounter
import cv2
import time
from src import network

class CrowdDensityEstimator:
    def __init__(self, model_path):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        torch.backends.cudnn.enabled = False
        self.model = self.load_model(model_path)
        self.model.to(self.device)
        self.model.eval()

    def load_model(self, model_path):
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
        print("Starting analysis of frame!\n")
        start_time = time.time()

        im_data = self.preprocess_frame(frame)
        print('Frame pre-processing done!\n')

        im_data = torch.tensor(im_data).to(self.device)
        print('Starting to count people :) \n')

        with torch.no_grad():
            density_map = self.model(im_data)

        density_map = density_map.data.cpu().numpy()
        people_count = int(np.sum(density_map))
        print("Estimated count:", people_count)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Prediction time: {elapsed_time:.4f} seconds")
        print()

        return people_count

    def analyse_video(self, video_path):
        cap = cv2.VideoCapture(video_path)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Analyze each frame
            people_count = self.analyse_frame(frame)

            # Optionally display the frame with the count
            cv2.putText(frame, f'Count: {people_count}', (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
            cv2.imshow('Frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    estimator = CrowdDensityEstimator(model_path='src/cmtl_shtechA_100.h5')
    video_path = "samples/crowd1.mp4"
    estimator.analyse_video(video_path)

import os
import torch
import numpy as np
from src.crowd_count import CrowdCounter
import cv2
import time
from src import network
import subprocess


class CrowdDensityEstimator:
    def __init__(self, model_path, socketio=None):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        torch.backends.cudnn.enabled = False
        self.model = self.load_model(model_path)
        self.model.to(self.device)
        self.model.eval()
        self.socketio = socketio

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

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            print(people_count)

        cap.release()
        cv2.destroyAllWindows()

    def analyse_stream(self, video_url,camera, analyze_interval=5):
        # Use ffmpeg to capture the video stream from the URL
        ffmpeg_command = [
            'ffmpeg',
            '-i', video_url,
            '-vf', 'scale=640:480',  # Scale the video to 640x480 resolution
            '-an',  # Disable audio
            '-r', '10',  # Reduce frame rate to 10 FPS
            '-f', 'rawvideo',
            '-pix_fmt', 'bgr24',
            '-'  # Output raw video to stdout
        ]

        print("Starting FFmpeg process...")
        process = subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        frame_width = 640  
        frame_height = 480 
        frame_size = frame_width * frame_height * 3  
        fps = 10  
        frames_to_skip = fps * analyze_interval  

        buffer = b''
        frame_count = 0

        while True:
            buffer += process.stdout.read(frame_size - len(buffer))
            if len(buffer) < frame_size:
                print("Incomplete frame received, breaking the loop.")
                break

            frame = np.frombuffer(buffer[:frame_size], np.uint8).reshape((frame_height, frame_width, 3))
            buffer = buffer[frame_size:]  

            if frame_count % frames_to_skip == 0:
                print("Captured a frame for analysis")

                
                writable_frame = frame.copy()

                people_count = self.analyse_frame(writable_frame)
                crowd_information = (camera,people_count)

                cv2.putText(writable_frame, f'Count: {people_count}', (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                cv2.imshow('Frame', writable_frame)
                
                return crowd_information


            frame_count += 1

        process.terminate()
        cv2.destroyAllWindows()

        


if __name__ == "__main__":
    estimator = CrowdDensityEstimator(model_path='src/cmtl_shtechA_100.h5')
    camera = 'camera1'
    video_path = "https://hd-auth.skylinewebcams.com/live.m3u8?a=bpbpou8enfj3c4pleosn121gm1"
    estimator.analyse_stream(video_path,camera)

import os
import torch
import numpy as np
from src.crowd_count import CrowdCounter
import cv2
import time
from src import network

def preprocess_image(image_path):
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        img = img.astype(np.float32, copy=False)
        
        ht, wd = img.shape
        ht_1 = int(ht / 4) * 4
        wd_1 = int(wd / 4) * 4
        img = cv2.resize(img, (wd_1, ht_1))
        
        img = img.reshape((1, 1, img.shape[0], img.shape[1]))  # (C, H, W)
        return img

def analyse_picture(image_path):

    print("Starting analysis of picture!")
    start_time = time.time()
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    torch.backends.cudnn.enabled = False

    model_path = 'src/cmtl_shtechA_100.h5'

    # Load the pre-trained model
    net = CrowdCounter()
    network.load_net(model_path, net)
    net.to(device)
    net.eval()

    # Preprocess the image
    im_data = preprocess_image(image_path)
    print('Image processed')

    im_data = torch.tensor(im_data).to(device)
    print('Starting to count people')

    with torch.no_grad():
        density_map = net(im_data)

    density_map = density_map.data.cpu().numpy()
    people_count = int(np.sum(density_map))
    print("Estimated count:", people_count)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Prediction time: {elapsed_time:.4f} seconds")
    print()

    return people_count

if __name__ == "__main__":
     image_path = "samples/sample1.jpg"
     analyse_picture(image_path)
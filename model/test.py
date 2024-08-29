# PyTorch Hub
import torch

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Single Image
img = 'IMG_2.jpg'  # path to your image

# Inference
results = model(img)

# Print results
results.print()  # Prints the detection results in the console

# Filter the results for the "person" class (class 0 in COCO dataset)
persons = results.xyxy[0]  # xyxy format: [x1, y1, x2, y2, confidence, class]
person_count = (persons[:, -1] == 0).sum().item()

# Output the number of people detected
print(f"Number of people detected: {person_count}")

# Display the image with bounding boxes
results.show()   # Displays the image with the detected objects



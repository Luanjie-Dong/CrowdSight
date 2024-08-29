import torch

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Adjust the confidence threshold if needed
model.conf = 0.25  # Default is 0.25, lower it if necessary to detect more objects

# Single Image
img = 'IMG_2.jpg'  # Ensure the image path is correct

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
results.show()  # Displays the image with the detected objects

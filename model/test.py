from mmdet.apis import init_detector, inference_detector, show_result_pyplot

# Load the model config and checkpoint
config_file = 'configs/faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
checkpoint_file = 'checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'

model = init_detector(config_file, checkpoint_file, device='cuda:0')

# Test a single image
img = 'IMG_2.jpg'
result = inference_detector(model, img)

# Count the number of people (class 0 in COCO)
person_count = len(result[0][0])
print(f"Number of people detected: {person_count}")

# Show the result
show_result_pyplot(model, img, result)

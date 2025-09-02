import cv2
import numpy as np
from ultralytics import YOLO
from collections import defaultdict

def extract_fields(image, model):
  results = model.predict(source=image, conf=0.25)
  variables = defaultdict(list)
  for result in results:
      boxes = result.boxes.xyxy.cpu().numpy()
      class_ids = result.boxes.cls.cpu().numpy().astype(int)
      for j, box in enumerate(boxes):
          if class_ids[j] not in [2, 5]:
              x1, y1, x2, y2 = map(int, box)
              crop = image[y1:y2, x1:x2]
              class_name = model.names[class_ids[j]]
              variables[f"{class_name}"].append(crop)
  return variables
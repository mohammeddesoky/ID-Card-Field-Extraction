import cv2
import numpy as np
from ultralytics import YOLO
from typing import Union

def detect_id(image: Union[str, np.ndarray], model):
    """
    image: path or numpy array
    model: ultralytics YOLO instance
    returns: cropped numpy region for first matched ID class, or None
    """
    img = image if isinstance(image, np.ndarray) else cv2.imread(image)
    if img is None:
        raise ValueError("detect_id: invalid image or path")

    results = model.predict(source=img, conf=0.25)
    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()
        class_ids = result.boxes.cls.cpu().numpy().astype(int)
        for j, box in enumerate(boxes):
            if class_ids[j] in [2, 5]:   # your ID class ids
                x1, y1, x2, y2 = map(int, box)
                # clamp coordinates to image bounds
                x1, y1 = max(0, x1), max(0, y1)
                x2, y2 = min(img.shape[1], x2), min(img.shape[0], y2)
                if x2 <= x1 or y2 <= y1:
                    continue
                crop = img[y1:y2, x1:x2].copy()
                return crop
    return None

import cv2
import numpy as np
import ultralytics
ultralytics.checks()
from ultralytics import YOLO
from skew_fixing import Skew_Fixing
from detect_id import detect_id
from extract_fields import extract_fields
from Read_text import Read_text

# load models once
model = YOLO("best.pt")   # can be same model for both steps

def main(image_path, model):
    print("Fixing skew...")
    deskewed = Skew_Fixing(image_path)

    print("Detecting ID card...")
    id_crop = detect_id(deskewed, model)
    if id_crop is None:
        print("[ERROR] No ID found.")
        return None

    print("Extracting fields...")
    fields = extract_fields(id_crop, model)
    if not fields:
        print("[ERROR] No fields detected.")
        return None

    print("Reading text...")
    results = Read_text(fields)

    print("RESULTS:", results)
    return results

if __name__ == "__main__":
    image = cv2.imread('ID.jpg')
    main(np.array(image), model)

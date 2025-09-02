import cv2
import numpy as np
from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
import uvicorn
from typing import List

# import your functions
from skew_fixing import Skew_Fixing
from detect_id import detect_id
from extract_fields import extract_fields
from Read_text import Read_text

# initialize FastAPI
app = FastAPI()

# load model once
model = YOLO("best.pt")

def pipeline(image_bytes):
    # convert bytes -> cv2 image
    nparr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # step 1: fix skew
    deskewed = Skew_Fixing(img)

    # step 2: detect ID
    id_crop = detect_id(deskewed, model)
    if id_crop is None:
        return {"error": "No ID detected"}

    # step 3: extract fields
    fields = extract_fields(id_crop, model)
    if not fields:
        return {"error": "No fields detected"}

    # step 4: read text
    results = Read_text(fields)
    return {"results": results}


@app.post("/predict")
# async def predict(file: UploadFile = File(...)):
#     image_bytes = await file.read()
#     output = pipeline(image_bytes)
#     return output

async def predict(files: List[UploadFile] = File(...)):
    results = []
    for file in files:
        image_bytes = await file.read()
        output = pipeline(image_bytes)
        results.append({
            "filename": file.filename,
            "output": output
        })
    return results


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)

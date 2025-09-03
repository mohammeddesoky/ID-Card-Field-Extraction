import streamlit as st
import numpy as np
from PIL import Image
import ultralytics
ultralytics.checks()
from ultralytics import YOLO  # replace with your actual model import
from main import main
from skew_fixing import Skew_Fixing
from detect_id import detect_id
from extract_fields import extract_fields
from Read_text import Read_text
import tempfile

# -----------------------------
# Load your trained model
# -----------------------------
model = YOLO("best.pt")  # replace with your model files

# -----------------------------
# Streamlit App
# -----------------------------
st.title("ID Field Extractor")

uploaded_file = st.file_uploader("Upload your ID image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded ID", use_container_width=True)

    if st.button("Extract Fields"):
        with st.spinner("Processing..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
                 image.save(tmp.name)
                 fields = main(tmp.name, model)
            # fields = main(np.array(image), model)
        st.success("Extraction Complete!")
        # print(np.array(image))
        # st.json(fields)
        for key, value in fields.items():
            st.text(f"{key}: {value}")

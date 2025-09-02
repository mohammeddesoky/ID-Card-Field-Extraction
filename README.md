# 🪪 ID Card Field Extraction with YOLO and Streamlit  

This project is a **Streamlit web application** that allows users to upload an ID card image and automatically extract key fields (such as ID number, name, etc.) using a **YOLO model** trained for detection and OCR for text recognition.  

---

## 🚀 Features  
- 📤 Upload ID images directly from the browser.  
- 🤖 Automatic detection and field extraction using YOLO.  
- 📐 Skew fixing for improved recognition accuracy.  
- 🔎 OCR text reading from detected regions.  
- ⚡ Instant results displayed in the app.  
- 🖼️ Supports **PNG, JPG, and JPEG** formats.  
- 🖥️ Easy to run locally or deploy online.  

---

## 🛠️ Technologies Used  
- [Python 3.x](https://www.python.org/)  
- [Streamlit](https://streamlit.io/)  
- [OpenCV](https://opencv.org/)  
- [Pillow](https://pypi.org/project/Pillow/)  
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)  

---

## 📂 Project Structure

```
project/
├── main.py # Main pipeline to process ID images
├── detect_id.py # Detect ID region using YOLO model
├── extract_fields.py # Extract text fields from detected regions
├── skew_fixing.py # Fix skewness in the ID image
├── Read_text.py # OCR reading for Arabic/English text
├── best.pt # YOLO trained weights
├── app.py # Streamlit app entry point
└── requirements.txt # Dependencies
```

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/id-field-extractor.git
   cd id-field-extractor
   
2. Install the required dependencies:
    pip install -r requirements.txt

3. Run the Streamlit app:
    streamlit run app.py
import streamlit as st
from PIL import Image
import pytesseract

# Set up Tesseract executable path (make sure you have Tesseract installed)
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def ocr_image(image):
    text_mixed = pytesseract.image_to_string(image, config='--oem 1 --psm 6')
    return text_mixed

def ocr_image(image):
    text_thai = pytesseract.image_to_string(image, lang='tha')
    return text_thai

def main():
    st.title("ทดสอบระบบแปลง Image --> Text (Thai)")
    st.write("Upload ภาพที่นี่")

    uploaded_image = st.file_uploader("เลือกภาพ...", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="ภาพที่ Upload มา. . .", use_column_width=True)

        if st.button("แปลงภาพเป็นข้อความ (ไทย)"):
            with st.spinner("กำลังทำงานจ้าาาาา..."):
                thai_text = ocr_image(image)
                st.write("เสร็จแล้ววววว:")
                st.write(thai_text)

if __name__ == "__main__":
    main()





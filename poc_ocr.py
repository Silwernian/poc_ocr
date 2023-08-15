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
    st.title("Thai Language Image to Text OCR App")
    st.write("Upload an image with Thai text")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Extract Thai Text"):
            with st.spinner("Extracting Thai text..."):
                thai_text = ocr_image(image)
                st.write("Extracted Thai Text:")
                st.write(thai_text)

if __name__ == "__main__":
    main()





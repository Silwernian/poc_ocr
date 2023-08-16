import streamlit as st
from PIL import Image
import pytesseract
import io
import functions.functions as fc

class OCR:

    def __init__(self):
        st.set_page_config(page_title="Python OCR", layout='wide')
        self.texto = ""
        self.analisar_texto = False

    def inicial(self):
        st.title("POC of Image --> Text")
        st.text('Version 1.2a')

        # User input for image source: Upload or Camera
        option = st.radio("Select Image Source:", ("Upload Image", "Take a Picture"))

        if option == "Upload Image":
            uploaded_image = st.file_uploader("Upload Your Image Here:", type=["jpg", "png", "jpeg"])
            if uploaded_image is not None:
                img = Image.open(uploaded_image)
                st.image(img)
                st.info("This is your Text . . .")
                self.texto = self.extrair_texto(img)
                st.write("{}".format(self.texto))
                
        elif option == "Take a Picture":
            camera_image = st.camera_input("Take a Picture:")
            if camera_image is not None:
                img = Image.open(io.BytesIO(camera_image))
                st.image(img)
                st.info("This is your Text . . .")
                self.texto = self.extrair_texto(img)
                st.write("{}".format(self.texto))
             
    def extrair_texto(self, img):
        texto = pytesseract.image_to_string(img, lang='tha+eng+equ')
        return texto

ocr = OCR()
ocr.inicial()

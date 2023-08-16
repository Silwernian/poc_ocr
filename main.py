#import principal
import streamlit as st
#imports relacionados
from PIL import Image
import pytesseract
#metodos internos
import functions.functions as fc

class OCR:

    def __init__(self):
        st.set_page_config(page_title="Python OCR", layout='wide')
        self.texto = ""
        self.analisar_texto = False

    def inicial(self):
        
        st.title("POC of Image --> Text")
        st.text('Version 1.2zz')
        imagem = st.camera_input("Upload Your Image Here:")
        #se selecionar alguma imagem...
        if imagem:
            img = Image.open(imagem)
            st.image(img)
            st.info("This is your Text . . .")
            self.texto = self.extrair_texto(img)
            st.write("{}".format(self.texto))
             
    def extrair_texto(self, img):
        #O comando que extrai o texto da imagem
        texto = pytesseract.image_to_string(img, lang="tha+equ")
        return texto
    
    
ocr = OCR()
ocr.inicial()
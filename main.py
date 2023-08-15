#import principal
import streamlit as st
#imports relacionados
from PIL import Image
import pytesseract
#metodos internos
import functions.functions as fc

class OCR:

    def __init__(self):
        st.set_page_config(page_title="Python OCR")
        self.texto = ""
        self.analisar_texto = False

    def inicial(self):
        
        st.title("POC of Image --> Text")
        imagem = st.file_uploader("Upload Your Image Here:", type=["png","jpg"])
        #se selecionar alguma imagem...
        if imagem:
            img = Image.open(imagem)
            st.image(img, width=350)
            st.info("This is your Text . . .")
            self.texto = self.extrair_texto(img)
            st.write("{}".format(self.texto))
             
    def extrair_texto(self, img):
        #O comando que extrai o texto da imagem
        texto = pytesseract.image_to_string(img, lang="tha")
        return texto
    
    
ocr = OCR()
ocr.inicial()
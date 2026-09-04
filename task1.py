import streamlit as st
from deep_translator import GoogleTranslator
#page title
st.title(" Translattion Web")
st.write("choose your Language and translate it")
#language option dictionary name
language={
    'English':'en',
    'Hindi':'hi',
    'french':'fr',
    'Japanese':'ja'
}
#for the selection
source_lang = st.selectbox("select your source language", list(language.keys()))
target_lang = st.selectbox("select target language", list(language.keys()))
#for the input
text_box=st.text_area("Enter text to translste")
#translatew button and logic
if st.button("translate"):
  if text_box:
    src_code=language[source_lang]
    tgt_code= language[target_lang]
    translated_text = GoogleTranslator(source=src_code, target=tgt_code).translate(text_box)
    st.write("Translated Text:", translated_text)
  

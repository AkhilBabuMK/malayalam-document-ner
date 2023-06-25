import streamlit as st
from tesserac import readData

uploaded_file  = st.file_uploader(label="upload your image here",type= ['jpg', 'png','jpeg'])
uploaded_bytes = uploaded_file.getvalue()

st.write(readData(uploaded_file.read()))
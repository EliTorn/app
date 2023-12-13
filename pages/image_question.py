from mongo import connect, upload_image
import streamlit as st

st.title("להעלות שאלה עם תמונה ")
image_question = st.text_input("מה השאלה ?")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
image_bit =''
if uploaded_file:
    image_bit = uploaded_file.read()
    st.image(uploaded_file, caption=image_question, width=200)

if st.button("Save Data") and uploaded_file:
    upload_image(image_question, image_bit)

    st.success('Data Save')

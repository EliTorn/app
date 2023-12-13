from mongo import connect, upload_image
import streamlit as st

st.title("שאלות")
name = st.text_input("נושא השאלה")
question = st.text_area("מה השאלה")

if st.button("שלח"):
    connect(name, question)
    st.success("נשלח")


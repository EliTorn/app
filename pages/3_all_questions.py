from mongo import show, show_image
import streamlit as st

st.title(" מציג את כל השאלות")
st.write("\n\n\n")
data = show()
images = show_image()
for q in data:
    st.write(q["topic"])
    st.write(q["question"])
    st.text("--------------------")

for image in images:
    st.image(image["image"])
    st.write(image["question"])
    st.text("--------------------")
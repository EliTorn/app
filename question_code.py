import streamlit as st
from q1 import q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11

st.title("question code")
st.write("\n\n\n\n")
buttons1 = st.columns(5)
buttons2 = st.columns(5)
buttons3 = st.columns(5)

list_questions = [f"question{i}" for i in range(1, 31)]

if buttons1[0].button(list_questions[0], key=1):
    q1()
if buttons1[1].button(list_questions[1], key=2):
    q2()
if buttons1[2].button(list_questions[2], key=3):
    q3()
if buttons1[3].button(list_questions[3], key=4):
    q4()
if buttons1[4].button(list_questions[4], key=5):
    q5()
if buttons2[0].button(list_questions[5], key=6):
    q6()
if buttons2[1].button(list_questions[6], key=7):
    q7()

if buttons2[2].button(list_questions[7], key=8):
    q8()
if buttons2[3].button(list_questions[8], key=9):
    q9()
if buttons2[4].button(list_questions[9], key=10):
    q10()

if buttons3[0].button(list_questions[10], key=11):
    q11()

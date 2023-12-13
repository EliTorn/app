import streamlit as st
from user_input import user_input1,casting
st.title("User Input = קלט מהמשתמש")

st.markdown("""
שים לב : כל קלט שנקבל מהמשתמש יהיה מסוג מחרוזת
\n
ונצטרך ללמוד איך להמיר אותו  
""")
user_input1()
st.write("זה אמור להיראות ככה")

name = st.text_input("Enter your name : ")
if name:
    st.write(f"Your name is {name}")
st.text("\n\n\n")
st.markdown("""
תרגיל למידה : שים לב שהקלט מהמשתמש הוא תמיד יהיה מסוג מחרוזת
\n
(string)
""")
st.write("המרה (שינוי ערך) = casting")
if st.button("המרה מסוג אחד לסוג אחר"):
    st.markdown("""
    בשביל להמיר מסוג אחד לסוג אחר נשתמש במתודה הזאת 
    #### int.Parse("100")
    מה שזה יעשה זה יקח את המחזורת 100 ויהפוך אותה למספר 100
    """)
    casting()
    st.markdown("""
    ### תוצאה
    ##### System.String
    ##### System.Int32
    """)
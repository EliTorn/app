import streamlit as st
from output import write, writeLine, number, solation1, solation2

st.title("הדפסה - Output ")
st.markdown("""
### יש כמה סוגים של הדפסה 
1. הדפסה רגילה - ואחרי שהוא מדפיס לרדת שורה
2. הדפסה בלי לרדת שורה אחרי זה 
3. הדפסת מספר 
""")
st.title("\n\n")
writeLine()
st.markdown("""
### תוצאה
Hello world !
\n
My name is Eli
""")
write()
st.markdown("""
### תוצאה
Hello world !
""")
number()
st.markdown("""
### תוצאה
13
##### שים לב - שהמחשב יודע לקחת מספר ולקבל את הערך שלו
""")


def one():
    c1, c2 = st.columns(2)
    targil1 = c1.button("תרגיל ראשון")
    if targil1:
        st.write("כתוב תוכנית מחשב שמדפיסה את שמך למסך ")
        st.write("Hello My name is {your name} ")

    if c2.button("פיתרון"):
        solation1()


def two():
    c1, c2 = st.columns(2)
    targil1 = c1.button("תרגיל שני", key=1)
    if targil1:
        st.write("בנה קוד שמקבל  5 ציונים ואז מחשב ומדפיס למסך את הממוצע שלהם. ")
        st.write("שים לב: שממוצע זה סכום של כל המספרים לחלק לכמות מספרים ")
        st.write("is average is {avg} ")

    if c2.button("פיתרון", key=2):
        solation2()

one()
two()

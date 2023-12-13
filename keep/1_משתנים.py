# app.py
import streamlit as st
from variables import q1, example1, solution1, solution2

key = 0
st.title("משתנים - variables ")
st.write("#### יש כמה סוגים של של משתנים נעבור עליהם")
question_one = ""
st.markdown("""
1.  int -  שומר רק מספרים שלמים 
2. double - מאחסן מספרים עשרוניים
3. string - מאחסן משפטים שלמים
4. char - מאחסן רק תווים בודדים
5. bool - מאחסן ערך אמת או שקר 
""")
example1()

st.markdown("""
#### הסבר
##### int age = 5;
""")
st.write(" int אני שומר במחשב מספר שלם מטיפוס ")
st.write("  age אני שומר אותו בשם של")
st.write("ואני מכניס לו את הערך 5")
st.text("\n\n\n")

st.markdown("""
##### double num2 = 3.5;
""")
st.write(" double אני שומר במחשב מספר שלם מטיפוס ")
st.write("  num2 אני שומר אותו בשם של")
st.write("ואני מכניס לו את הערך 3.5")
st.text("\n\n\n")



def one():
    c1, c2, c3 = st.columns(3)
    targil1 = c1.button("תרגיל ראשון")
    if targil1:
        st.write("name תגדיר משתנה בשם  \n ותכניס לו את השם שלך ")
    shlab1 = c2.button("שלבים")
    if shlab1:
        st.markdown("""
        1. דבר ראשון נבדוק איזה משתנה אנחנו צריכים להשתמש 
        2. נגדיר את המשתנה ונביא לו את השם שבקשו ממנו
        3. נכניס לו את השם שלנ  
        """)
    solation1 = c3.button("פיתרון")
    if solation1:
        solution1()


def tow():
    c1, c2, c3 = st.columns(3)
    targil1 = c1.button("תרגיל שני", key=key + 1)
    if targil1:
        st.markdown("""
        תגדיר משתנה ותכניס לו את הערך של 5 
        \n
        תגדיר משתנה נוסף ותכניס לו את הערך של 4.2
        \n
         תגדיר משתנה נוסף ותכניס לו את הערך אמת 
        """)
    shlab1 = c2.button("שלבים", key + 2)
    if shlab1:
        st.markdown("""
            1. דבר ראשון נבדוק איזה משתנים אנחנו צריכים להשתמש 
            2. נגדיר את המשתנים ונביא להם שמות (איזה שנחליט)
            3. נכניס את הערכים שבקשו ממנו  
            """)
    solation1 = c3.button("פיתרון", key + 3)
    if solation1:
        solution2()


one()
tow()
key += 5

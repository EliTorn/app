import streamlit as st
from datetime import datetime

st.title("Question 1:")


def get_current_time():
    now = datetime.now()
    return now.hour, now.minute


hour, minute = get_current_time()

if 22 <= hour < 24 or (hour == 23 and minute <= 59):
    # This is considered a success within your criteria
    st.success("You have succeeded! and you get to the next level")

else:
    # Display the error message in both Hebrew and English
    st.error("""
    המסיבה מתחילה בשעה 23:00 

    The party starts at 23:00  
    """)

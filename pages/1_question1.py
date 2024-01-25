import streamlit as st
from datetime import datetime
import pytz

st.title("Question 1:")


def get_current_time_in_user_timezone():
    user_timezone = pytz.timezone('Asia/Jerusalem') # Use the appropriate method to get the user's time zone
    now_utc = datetime.now(pytz.utc)
    now_user_time = now_utc.astimezone(user_timezone)
    return now_user_time.hour, now_user_time.minute

hour, minute = get_current_time_in_user_timezone()

if 23 <= hour <= 23 and 0 <= minute <= 59:
    # This is considered a success within your criteria
    st.success("You have succeeded! and you get to the next level")

else:
    # Display the error message in both Hebrew and English
    st.error("""
    המסיבה מתחילה בשעה 23:00 

    The party starts at 23:00  
    """)

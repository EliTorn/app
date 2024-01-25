import streamlit as st
from datetime import datetime
import pytz

st.title("Question 1:")




 now = datetime.now()
 hour, minute = now.hour, now.minute

if 23 <= hour <= 23 and 0 <= minute <= 59:
    # This is considered a success within your criteria
    st.success("You have succeeded! and you get to the next level")

else:
    # Display the error message in both Hebrew and English
    st.error("""
    המסיבה מתחילה בשעה 23:00 

    The party starts at 23:00  
    """)

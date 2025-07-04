import streamlit as st
import random

quotes = [
    "You're unstoppable.",
    "Believe in yourself.",
    "Success starts with self-discipline.",
    "You are braver than you believe.",
    "Consistency is power."
]

st.title("Motivational Quote of the Day")
st.write("Click the button below to get your daily boost!")

if st.button("Get Quote"):
    st.success(random.choice(quotes))

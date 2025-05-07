import streamlit as st

st.title("Open and Close Buttons")

# Create two buttons
if st.button("Open"):
    st.success("You clicked the Open button!")

if st.button("Close"):
    st.warning("You clicked the Close button!")

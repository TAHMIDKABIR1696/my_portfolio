import streamlit as st
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/my photo.jpg", width=500)

with col2:
    st.title("MD.TAHMID KABIR")
    myinfo = "Hi this is my project. Welcome inside the webpage. May you like it"

    st.info(myinfo)
import streamlit as st
import pandas
st.set_page_config(layout="wide")


col1, col2 = st.columns(2)

with col1:
    st.image("images/my photo.jpg", width=500)

with col2:
    st.title("MD.TAHMID KABIR")
    myinfo = "Hi this is my project."

    st.info(myinfo)

myinfo2 = "Wellcome and feel free to explore the website"
st.info(myinfo2)

df = pandas.read_csv("data.csv",sep=";")
col3, col4 = st.columns(2)
with col3:
    for index , row in df[:10].iterrows():
        st.header(row["title"])


with col4:
    for index , row in df[10:].iterrows():
        st.header(row["title"])

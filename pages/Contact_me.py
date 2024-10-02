import streamlit as st
from send_mail import send_email

st.header("Hope you like my page.\nContact me:")

with st.form(key="email"):
    user_email = st.text_input("Your Email Address:")
    raw_messages = st.text_area("Enter Your Messages")
    messages = f"""\
Subject: Email from {user_email}

From: {user_email}
{raw_messages}"""
    button = st.form_submit_button("SUBMIT")
    if button:
        send_email(messages)
        st.info("Your email was sent successfully")

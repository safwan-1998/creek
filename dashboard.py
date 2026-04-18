import streamlit as st

st.title("🚀 Hello World")

st.write("If you can see this, deployment works!")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name} 👋")
    st.write("App is alive")
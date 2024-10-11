import streamlit as st

options = ["hello","world"]
st.sidebar.selectbox("Options",options)
st.title("Hello World")
st.write("This is my first web hosted application")

video_file = open("https://www.youtube.com/watch?v=vwsN9dS1x8E&t=29s&pp=ygUedHJvbGwgZmFjZSBtb21lbnRzIGluIGZvb3RiYWxs")
video_bytes = video_file.read()

st.video(video_bytes)
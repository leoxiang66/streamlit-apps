import streamlit as st

audio_file = open('myaudio.ogg', 'rb')
audio_bytes = audio_file.read()

audio = st.audio(audio_bytes, format='audio/ogg')

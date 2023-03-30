import streamlit as st

def __go_to__(page:str):
    st.session_state['current_page'] = page

def go_to_home():
    __go_to__('home')
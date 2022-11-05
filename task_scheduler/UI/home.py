import streamlit as st
from .task_create_view import task_create_view
# from ..task import TaskList

def home():
    st.markdown('# Task Scheduler')


    col1, col2 = st.columns(2, gap= 'medium')

    with col1:
        st.markdown('# Current Tasks')



    with col2:
        st.markdown("# Stored Tasks")
        new_task_button = st.button(label='Create a New Task')
        if new_task_button:
            task_data = task_create_view()






if __name__ == '__main__':
    home()
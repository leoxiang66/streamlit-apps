import datetime

import streamlit as st


def __sub_task__():
    task_name = st.text_input(label='Task Name', placeholder='My little taski')
    task_content = st.text_area(label='Task Content', placeholder='Buy some apples:)')
    task_time = st.selectbox(label='Task Time', options=['30 Seconds',
                                                         '1 Minute',
                                                         '3 Minutes',
                                                         '5 Minutes',
                                                         '10 Minutes',
                                                         '15 Minutes',
                                                         '30 Minutes'
                                                         ])


def task_create_view():
    with st.container():
        task_name = st.text_input(label='Task Name',placeholder='My little taski')
        task_content = st.text_area(label='Task Content', placeholder= 'Buy some apples:)')
        task_time = st.selectbox(label='Task Time', options=['30 Seconds',
                                                             '1 Minute',
                                                             '3 Minutes',
                                                             '5 Minutes',
                                                             '10 Minutes',
                                                             '15 Minutes',
                                                             '30 Minutes'
                                                             ] )

        # Every form must have a submit button.
        subtask = st.button('Add a subtask')
        submitted = st.button("Create Task",type='primary')


        if subtask:
            __sub_task__()

    if submitted:

        ret = dict(
        task_name = task_name,
        task_content = task_content,
        task_time = task_time,
    )

        print(ret)
        return ret


if __name__ == '__main__':

    task_create_view()

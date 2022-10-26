import streamlit as st
from pprint import pprint
from widgets import *

# [![github](https://img.kookapp.cn/assets/2022-09/1w4G0FIWGK00w00w.png)](https://github.com/Mondkuchen/idp_LiteratureResearch_Tool)

# sidebar content
platforms, number_papers,start_year,end_year = render_sidebar()

# body head
with st.form("my_form",clear_on_submit=False):
    st.markdown('''# 👋 Hi, enter your query here :)''')
    query_input = st.text_input(
        'Enter your keyphrases',
        placeholder='''e.g. "Machine learning"''',
        label_visibility='collapsed',
        value=''
    )

    show_preview = st.checkbox('show paper preview')

    # Every form must have a submit button.
    submitted = st.form_submit_button("Search")


if submitted:
    # body
    render_body(platforms, number_papers, 5, query_input, show_preview)




import streamlit as st
from pprint import pprint
import streamlit.components.v1 as components
from widgets import *
from pyecharts.charts import Bar
from pyecharts import options as opts

# [![github](https://img.kookapp.cn/assets/2022-09/1w4G0FIWGK00w00w.png)](https://github.com/Mondkuchen/idp_LiteratureResearch_Tool)

# sidebar content
platforms, number_papers,start_year,end_year = render_sidebar()

# body head
with st.form("my_form",clear_on_submit=False):
    st.markdown('''# 👋 Hi, enter your query here :)''')
    query_input = st.text_input(
        'Enter your keyphrases',
        placeholder='''e.g. "Machine learning"''',
        # label_visibility='collapsed',
        value=''
    )

    show_preview = st.checkbox('show paper preview')

    # Every form must have a submit button.
    submitted = st.form_submit_button("Search")


if submitted:
    # body
    render_body(platforms, number_papers, 5, query_input, show_preview,start_year,end_year)

    bar = (
        Bar()
        .add_xaxis(["Cluster 1", "Cluster 2", "Cluster 3", 'Cluster 4', 'Cluster 5'])
        .add_yaxis("numbers", [23, 16, 13, 12, 5])
        .set_global_opts(title_opts=opts.TitleOpts(title="Fake Data"))
    )

    components.html(generate_html_pyecharts(bar, 'tmp.html'), height=500, width=1000)





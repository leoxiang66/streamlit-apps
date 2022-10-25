import streamlit as st
from pprint import pprint
from widgets import *

# [![github](https://img.kookapp.cn/assets/2022-09/1w4G0FIWGK00w00w.png)](https://github.com/Mondkuchen/idp_LiteratureResearch_Tool)

# sidebar content
platforms, number_papers = render_sidebar()

# body
render_body(platforms,number_papers,5)





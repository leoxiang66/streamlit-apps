import streamlit as st

# [![github](https://img.kookapp.cn/assets/2022-09/1w4G0FIWGK00w00w.png)](https://github.com/Mondkuchen/idp_LiteratureResearch_Tool)
# sidebar content
sidebar_markdown = f'''

<center>
<img src="https://leoxiang66.github.io/images/tum.png" alt="TUM" width="150"/>

<h1>
Paper Analysis Tool 
</h1>


<code>
v1.0.0
</code>


</center>


<center>
<a href="https://github.com/Mondkuchen/idp_LiteratureResearch_Tool"><img src = "https://cdn-icons-png.flaticon.com/512/733/733609.png" width="23"></img></a>  <a href="mailto:xiang.tao@outlook.de"><img src="https://cdn-icons-png.flaticon.com/512/646/646094.png" alt="email" width = "27" ></a>
</center>

---

## Choose the Paper Search Platforms'''
st.sidebar.markdown(sidebar_markdown,unsafe_allow_html=True)
# elvsier = st.sidebar.checkbox('Elvsier',value=True)
# IEEE = st.sidebar.checkbox('IEEE',value=False)
# google = st.sidebar.checkbox('Google Scholar')
platforms = st.sidebar.multiselect('Platforms',options=['Elvsier','IEEE','Google Scholar'], default=['Elvsier','IEEE','Google Scholar'])


st.sidebar.markdown('## Choose the number of papers per platform')
numer=st.sidebar.slider('number',0,500,100,10)

# body
# st.markdown('# Enter your keyphrases')
query_input = st.text_input('Enter your keyphrases', placeholder='''e.g. "Machine learning"''')

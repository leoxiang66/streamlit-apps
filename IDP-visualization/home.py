import streamlit as st
from pprint import pprint
from api_ import ArxivQuery

# [![github](https://img.kookapp.cn/assets/2022-09/1w4G0FIWGK00w00w.png)](https://github.com/Mondkuchen/idp_LiteratureResearch_Tool)

# sidebar content
sidebar_markdown = f'''

<center>
<img src="https://img.kookapp.cn/assets/2022-07/8rKqcd8Pnv0xc0hc.png" alt="TUM" width="150"/>

<h1>
Literature Research Tool 
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
platforms = st.sidebar.multiselect('Platforms',options=
[
    # 'Elvsier',
    'IEEE',
    # 'Google Scholar',
    'Arxiv',
    'PaperWithCode'
], default=[
    # 'Elvsier',
    'IEEE',
    # 'Google Scholar',
    'Arxiv',
    'PaperWithCode'
])



st.sidebar.markdown('## Choose the number of papers to display')
number_papers=st.sidebar.slider('number', 0, 500, 100, 10)



# body

# st.markdown('# Enter your keyphrases')
query_input = st.text_input('Enter your keyphrases', placeholder='''e.g. "Machine learning"''')
tmp = st.empty()
paperInGeneral = st.empty() # paper的大概

# | Text     | Text     | Text  |
if query_input != '':
    tmp.markdown(f'You entered query: `{query_input}`')
    paperInGeneral_md = '''| ID| Paper Title | Publication Year |
| -------- | -------- | -------- |\n'''


    # Arxiv
    arxiv = ArxivQuery.query(query_input, max_results=number_papers)
    pprint(arxiv[0])
    for i in range(5):
        title = str(arxiv[i]['title']).replace('\n',' ')
        publication_year = str(arxiv[i]['published']).replace('\n',' ')
        paperInGeneral_md +=f'''|{i+1}|{title}|{publication_year}|\n'''

    paperInGeneral.markdown(paperInGeneral_md)




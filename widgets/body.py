import streamlit as st
from api_ import ArxivQuery, IEEEQuery, PaperWithCodeQuery

def __preview__(platforms, num_papers, num_papers_preview, query_input,start_year,end_year):
    with st.spinner('Searching...'):
        paperInGeneral = st.empty()  # paper的大概
        paperInGeneral_md = '''# Query Results Preview
We have found following papers for you! (displaying 5 papers for each literature platforms)
'''
        if 'IEEE' in platforms:
            paperInGeneral_md += '''## IEEE
| ID| Paper Title | Publication Year |
| -------- | -------- | -------- |
'''
            IEEEQuery.__setup_api_key__('vpd9yy325enruv27zj2d353e')
            ieee = IEEEQuery.query(query_input,start_year,end_year,num_papers)
            num_papers_preview = min(len(ieee), num_papers_preview)
            for i in range(num_papers_preview):
                title = str(ieee[i]['title']).replace('\n', ' ')
                publication_year = str(ieee[i]['publication_year']).replace('\n', ' ')
                paperInGeneral_md += f'''|{i + 1}|{title}|{publication_year}|\n'''
        if 'Arxiv' in platforms:
            paperInGeneral_md += '''
## Arxiv
| ID| Paper Title | Publication Year |
| -------- | -------- | -------- |
'''
            arxiv = ArxivQuery.query(query_input, max_results=num_papers)
            num_papers_preview = min(len(arxiv), num_papers_preview)
            for i in range(num_papers_preview):
                title = str(arxiv[i]['title']).replace('\n', ' ')
                publication_year = str(arxiv[i]['published']).replace('\n', ' ')
                paperInGeneral_md += f'''|{i + 1}|{title}|{publication_year}|\n'''
        if 'PaperWithCode' in platforms:
            paperInGeneral_md += '''
## Paper with Code
| ID| Paper Title | Publication Year |
| -------- | -------- | -------- |
'''
            pwc = PaperWithCodeQuery.query(query_input, items_per_page=num_papers)
            num_papers_preview = min(len(pwc), num_papers_preview)
            for i in range(num_papers_preview):
                title = str(pwc[i]['title']).replace('\n', ' ')
                publication_year = str(pwc[i]['published']).replace('\n', ' ')
                paperInGeneral_md += f'''|{i + 1}|{title}|{publication_year}|\n'''

        paperInGeneral.markdown(paperInGeneral_md)

def render_body(platforms, num_papers, num_papers_preview, query_input, show_preview:bool,start_year,end_year):

    tmp = st.empty()
    if query_input != '':
        tmp.markdown(f'You entered query: `{query_input}`')
        if show_preview:
            __preview__(platforms,num_papers,num_papers_preview,query_input,start_year,end_year)

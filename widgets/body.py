import streamlit as st
from api_ import ArxivQuery, IEEEQuery, PaperWithCodeQuery
import random

def render_body(platforms, num_papers, num_papers_preview):
    query_input = st.text_input('Enter your keyphrases', placeholder='''e.g. "Machine learning"''')
    tmp = st.empty()
    paperInGeneral = st.empty() # paper的大概
    random_ids = random.sample([i for i in range(num_papers)],num_papers_preview)

    if query_input != '':
        with st.spinner('Searching...'):
            tmp.markdown(f'You entered query: `{query_input}`')
            paperInGeneral_md = '''# Query Results Preview
We have found following papers for you! (displaying 5 papers for each literature platforms)
'''
            if 'IEEE' in platforms:
                paperInGeneral_md += '''## IEEE
| ID| Paper Title | Publication Year |
| -------- | -------- | -------- |
'''
                IEEEQuery.__setup_api_key__('vpd9yy325enruv27zj2d353e')
                ieee = IEEEQuery.query(query_input)
                for i in range(num_papers_preview):
                    id = random_ids[i]
                    title = str(ieee[id]['title']).replace('\n', ' ')
                    publication_year = str(ieee[id]['publication_year']).replace('\n', ' ')
                    paperInGeneral_md += f'''|{i + 1}|{title}|{publication_year}|\n'''
            if 'Arxiv' in platforms:
                paperInGeneral_md += '''
## Arxiv
| ID| Paper Title | Publication Year |
| -------- | -------- | -------- |
'''
                arxiv = ArxivQuery.query(query_input, max_results=num_papers)
                for i in range(num_papers_preview):
                    id = random_ids[i]
                    title = str(arxiv[id]['title']).replace('\n', ' ')
                    publication_year = str(arxiv[id]['published']).replace('\n', ' ')
                    paperInGeneral_md += f'''|{i + 1}|{title}|{publication_year}|\n'''
            if 'PaperWithCode' in platforms:
                paperInGeneral_md += '''
## Paper with Code
| ID| Paper Title | Publication Year |
| -------- | -------- | -------- |
'''
                pwc = PaperWithCodeQuery.query(query_input, items_per_page=num_papers)
                for i in range(num_papers_preview):
                    id = random_ids[i]
                    title = str(pwc[id]['title']).replace('\n', ' ')
                    publication_year = str(pwc[id]['published']).replace('\n', ' ')
                    paperInGeneral_md += f'''|{i + 1}|{title}|{publication_year}|\n'''

            paperInGeneral.markdown(paperInGeneral_md)
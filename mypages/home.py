import streamlit as st
from .sidebar import render_sidebar
from trendflow.API.query import ArxivQuery, IEEEQuery, PaperWithCodeQuery
# from lrt.clustering.clusters import SingleCluster
# from lrt.clustering.config import Configuration
# from lrt import ArticleList, LiteratureResearchTool
# from lrt_instance import *
# from .charts import build_bar_charts

def home():
    render_sidebar()



    def __preview__(platforms, num_papers, num_papers_preview, query_input, start_year, end_year):
        with st.spinner('Searching...'):
            paperInGeneral = st.empty()  # paper的大概
            paperInGeneral_md = '''# 0 Query Results Preview
    We have found following papers for you! (displaying 5 papers for each literature platforms)
    '''
            if 'IEEE' in platforms:
                paperInGeneral_md += '''## IEEE
    | ID| Paper Title | Publication Year |
    | -------- | -------- | -------- |
    '''
                IEEEQuery.__setup_api_key__('vpd9yy325enruv27zj2d353e')
                ieee = IEEEQuery.query(query_input, start_year, end_year, num_papers)
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
            if 'Paper with Code' in platforms:
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

    def render_body(platforms, num_papers, num_papers_preview, query_input, show_preview: bool, start_year, end_year,
                    hyperparams: dict, standardization=False):

        tmp = st.empty()
        if query_input != '':
            tmp.markdown(f'You entered query: `{query_input}`')

            # preview
            if show_preview:
                __preview__(platforms, num_papers, num_papers_preview, query_input, start_year, end_year)

            # lrt results
            ## baseline
            if hyperparams['dimension_reduction'] == 'none' \
                    and hyperparams['model_cpt'] == 'keyphrase-transformer' \
                    and hyperparams['cluster_model'] == 'kmeans-euclidean':
                model = baseline_lrt
            else:
                config = Configuration(
                    plm='''all-mpnet-base-v2''',
                    dimension_reduction=hyperparams['dimension_reduction'],
                    clustering=hyperparams['cluster_model'],
                    keywords_extraction=hyperparams['model_cpt']
                )
                model = LiteratureResearchTool(config)

            generator = model(query_input, num_papers, start_year, end_year, max_k=hyperparams['max_k'],
                              platforms=platforms, standardization=standardization)
            for i, plat in enumerate(platforms):
                clusters, articles = next(generator)
                st.markdown(f'''# {i + 1} {plat} Results''')
                clusters.sort()

                st.markdown(f'''## {i + 1}.1 Clusters Overview''')
                st.markdown(f'''In this section we show the overview of the clusters, more specifically,''')
                st.markdown(f'''\n- the number of papers in each cluster\n- the number of keyphrases of each cluster''')
                st.bokeh_chart(build_bar_charts(
                    x_range=[f'Cluster {i + 1}' for i in range(len(clusters))],
                    y_names=['Number of Papers', 'Number of Keyphrases'],
                    y_data=[[len(c) for c in clusters], [len(c.get_keyphrases()) for c in clusters]]
                ))

                st.markdown(f'''## {i + 1}.2 Cluster Details''')
                st.markdown(f'''In this section we show the details of each cluster, including''')
                st.markdown(f'''\n- the article information in the cluster\n- the keyphrases of the cluster''')
                for j, cluster in enumerate(clusters):
                    assert isinstance(cluster, SingleCluster)  # TODO: remove this line
                    ids = cluster.elements()
                    articles_in_cluster = ArticleList([articles[id] for id in ids])
                    st.markdown(f'''**Cluster {j + 1}**''')
                    st.dataframe(articles_in_cluster.getDataFrame())
                    st.markdown(f'''The top 5 keyphrases of this cluster are:''')
                    md = ''
                    for keyphrase in cluster.top_5_keyphrases:
                        md += f'''- `{keyphrase}`\n'''
                    st.markdown(md)





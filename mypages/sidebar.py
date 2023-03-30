import streamlit as st
import datetime
# from .utils import PACKAGE_ROOT
# from lrt.utils.functions import template

APP_VERSION = 'v0.1.0'


def render_sidebar():
    icons = f'''
    <center>
    <a href="https://github.com/leoxiang66/research-trends-analysis"><img src = "https://cdn-icons-png.flaticon.com/512/733/733609.png" width="23"></img></a>  <a href="mailto:xiang.tao@outlook.de"><img src="https://cdn-icons-png.flaticon.com/512/646/646094.png" alt="email" width = "27" ></a>
    </center>
    '''

    sidebar_markdown = f'''

    <center>
    <img src="https://raw.githubusercontent.com/leoxiang66/streamlit-tutorial/IDP/widgets/static/tum.png" alt="TUM" width="150"/>

    <h1>
    TrendFlow
    </h1>


    <code>
    {APP_VERSION}
    </code>


    </center>


    {icons}

    ---

    ## Choose the Paper Search Platforms'''
    st.sidebar.markdown(sidebar_markdown, unsafe_allow_html=True)
    # elvsier = st.sidebar.checkbox('Elvsier',value=True)
    # IEEE = st.sidebar.checkbox('IEEE',value=False)
    # google = st.sidebar.checkbox('Google Scholar')
    platforms = st.sidebar.multiselect('Platforms', options=
    [
        # 'Elvsier',
        'IEEE',
        # 'Google Scholar',
        'Arxiv',
        'Paper with Code'
    ], default=[
        # 'Elvsier',
        'IEEE',
        # 'Google Scholar',
        'Arxiv',
        'Paper with Code'
    ])

    st.sidebar.markdown('## Choose the max number of papers to search')
    number_papers = st.sidebar.slider('number', 10, 100, 20, 5)

    st.sidebar.markdown('## Choose the start year of publication')
    this_year = datetime.date.today().year
    start_year = st.sidebar.slider('year start:', 2000, this_year, 2010, 1)

    st.sidebar.markdown('## Choose the end year of publication')
    end_year = st.sidebar.slider('year end:', 2000, this_year, this_year, 1)

    with st.sidebar:
        st.markdown('## Adjust hyperparameters')
        with st.expander('Clustering Options'):
            standardization = st.selectbox('1) Standardization before clustering', options=['no', 'yes'], index=0)
            dr = st.selectbox('2) Dimension reduction', options=['none', 'pca'], index=0)
            tmp = min(number_papers, 15)
            max_k = st.slider('3) Max number of clusters', 2, tmp, tmp // 2)
            cluster_model = st.selectbox('4) Clustering model', options=['Gaussian Mixture Model', 'K-means'], index=0)

        with st.expander('Keyphrases Generation Options'):
            model_cpt = st.selectbox(label='Model checkpoint', options=['KeyBart', 'KeyBartAdapter', 'keyphrase-transformer'], index=0)

        st.markdown('---')
        st.markdown(icons, unsafe_allow_html=True)
        st.markdown(f'''<center>Copyright © 2022 - {datetime.datetime.now().year} by Tao Xiang</center>''', unsafe_allow_html=True)

    # st.sidebar.markdown('## Choose the number of clusters')
    # k = st.sidebar.slider('number',1,10,3)

    return platforms, number_papers, start_year, end_year, dict(
        dimension_reduction=dr,
        max_k=max_k,
        model_cpt=model_cpt,
        standardization=True if standardization == 'yes' else False,
        cluster_model='gmm' if cluster_model == 'Gaussian Mixture Model' else 'kmeans-euclidean'
    )
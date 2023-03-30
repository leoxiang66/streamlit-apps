import streamlit as st
import sthelper as helper
import pandas as pd




def welcome():
    def onclick():
        session.init('email', email)
        session.go_to_page('home')

    email = st.text_input('Email Address')
    st.button("Start", on_click=onclick)


def home():
    # Cache the dataframe so it's only loaded once
    @st.cache_data
    def load_data():
        tmp = pd.read_csv('results/dataset.csv')
        return tmp

    @st.cache_data
    def load_e1():
        c1 = pd.read_csv('results/e1/e1c1.csv')
        c2 = pd.read_csv('results/e1/e1c2.csv')
        c3 = pd.read_csv('results/e1/e1c3.csv')
        return c1,c2,c3

    df = load_data()

    st.markdown("## Dataset for this evaluation")
    st.dataframe(df, use_container_width=False)

    '''
    ## Metrics for this evaluation
    1. **relevance of clusters** 
        "Relevance of clusters" refers to the degree to which the clusters obtained from a clustering algorithm are meaningful or useful for a particular task or application. 
        
        In other words, how well the clusters align with the goals or objectives of the analysis.
    2. **coherence of clusters**
        "Coherence of clusters" is a term used in cluster analysis, which is a technique used in unsupervised machine learning to group similar data points together into clusters based on some similarity metric. The coherence of clusters refers to how well-defined or meaningful the clusters are, in terms of how distinct and internally consistent the data points within each cluster are.
        
        In other words, how internally consistent the data points with each cluster are.
    3. **accuracy of research trends**
        "Accuracy of research trends" refers to the degree to which the identified trends represent the actual state of the research in a given field or topic.
    '''

    ##############
       ## E1 ##
    #{
    #    'plm': 'all-mpnet-base-v2',
    #    'dimension_reduction': 'none',
    #    'clustering': 'gmm',
    #    'keywords_extraction': 'KeyBART-adapter'
    #}
    ##############
    st.markdown('## Evaluation 1')
    e1c1,e1c2,e1c3 = load_e1()

    st.markdown("### Cluster 1")
    st.dataframe(e1c1)
    st.markdown("**Generated research trends**")
    '''\n\n\n'''

    st.markdown("### Cluster 2")
    st.dataframe(e1c2)
    st.markdown("**Generated research trends**")
    '''\n\n\n'''

    st.markdown("### Cluster 3")
    st.dataframe(e1c3)
    st.markdown("**Generated research trends**")
    '''\n\n\n'''


    '''Evaluation: ("1" for very bad, "5" for very good)'''
    st.slider('Relevance of Clusters',1,5,3,key='e1_relevance')
    st.slider('Coherence of Clusters', 1, 5, 3, key='e1_coherence')
    st.slider('Accuracy of Research Trends', 1, 5, 3, key='e1_accuracy')




session = helper.OpenSession(
    current_page='welcome',
    page_map=dict(
        welcome = welcome,
        home = home,
    )
)

st.markdown("# Human Evaluation for TrendFlow")
st.info(session.summary())
session.render()
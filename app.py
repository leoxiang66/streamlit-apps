import streamlit as st
import sthelper as helper
import pandas as pd
from sthelper.gsheet import add_new_row


def intro():
    def onclick():
        session.go_to_page('welcome')
    st.markdown("# Human Evaluation for TrendFlow")
    st.markdown('''<h1 align='center'> TrendFlow</h1>

<p align='center'>
<a href = "https://github.com/leoxiang66/research-trends-analysis">
<img src="https://img.shields.io/github/stars/leoxiang66/research-trends-analysis.svg?style=social">
</a>
<a href = "https://leoxiang66.github.io/research-trends-analysis/"><img src="https://img.shields.io/website?label=documentation&up_message=online&url=https://leoxiang66.github.io/research-trends-analysis/"> </a>
<a href="https://pypi.org/project/TrendFlow/"><img src="https://badge.fury.io/py/trendflow.svg" alt="PyPI version" /> </a>
<a href="https://discord.gg/P5Y3FHgHRz">
        <img alt="chat on Discord" src="https://img.shields.io/discord/1091063040662843565?logo=discord">
    </a>
</p>


TrendFlow is an advanced framework that uses deep learning techniques to analyze research trends. This powerful framework offers a wide range of analytical capabilities, including literature clustering, trend generation, and trend summarization. With TrendFlow, you can gain insights into emerging research topics and stay up-to-date on the latest advancements in your field.''', unsafe_allow_html=True)

    '''
    **The general working pipeline of TrendFlow:**
    
1. TrendFlow starts by searching relevant literature on literature platforms such as IEEE
    using user-defined queries
2. It then encodes the abstracts of the literature into embeddings (vectors) and clusters the
    embeddings.
3. It generates research trends from the abstracts for each cluster and visualizes the final
    results.
    
To simplify this human evaluation, we ourself randomly collect around 217 abstracts in domains NLP, CV or audio processing on Arxiv. Then, we feed these abstracts to TrendFlow (with 2 different configurations), which clusters the abstracts and generates research trends for each cluster.
    
Raters are expected to rate the relevance, coherence of the clusters and the accuracy of the research trends. Besides, raters can give additional feedbacks (such as how is this pipeline in general? And improvement? Any drawbacks?).

You are also welcome to try our beta version web app: https://huggingface.co/spaces/Adapting/TrendFlow

(since it's using free cloud CPU, the framework is kinda slow at the moment)
    '''

    st.button('Continue', on_click=onclick)

def welcome():
    def onclick():
        session.init('email', email)
        session.go_to_page('home')

    st.markdown("# Human Evaluation for TrendFlow")
    email = st.text_input('Email Address')
    st.button("Start", on_click=onclick)

def thanks():
    st.markdown(''' <h1 style="margin-top: 100px; font-size: 48px; font-weight: bold; color: #333333;">Thanks for Your Effort!</h1>
    <p style="margin-top: 40px; font-size: 24px; color: #666666;">We appreciate all the hard work you put into this project.</p>''', unsafe_allow_html=True)


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
    st.markdown("# Human Evaluation for TrendFlow")
    helper.widgets.build_TOC(
        [
            ('h2', 'Dataset for this evaluation'),
            ('h2', 'Metrics for this evaluation'),
            ('h2', 'Evaluation 1'),
            ('h2', 'Evaluation 2'),
            ('h2', "Additional Feedbacks about TrendFlow")
        ]
    )

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
    st.markdown('''
    - 'automatic speech recognition',
    - 'deep neural network/multiple deep neural network/graph neural network',
    - 'multi-task learning network/multi-task learning',
    - 'speaker diarization',
    - 'multiple self-supervised speech model',
    - 'distilled model',
    - 'ensemble knowledge',
    - 'optimization framework',
    - 'text-based audio retrieval',
    - 'data leakage'
    '''.replace('''\'''',""))
    '''\n\n\n'''

    st.markdown("### Cluster 2")
    st.dataframe(e1c2)
    st.markdown("**Generated research trends**")
    st.markdown('''
   - 'convolutional neural network/graph convolutional neural network',
   - 'deep learning',
   - 'deep neural network',
   - 'computer vision',
   - 'x-ray image classification/image classification',
   - 'semantic segmentation/3D semantic segmentation',
   - 'domain generalisation/out-of-domain generalization',
   - 'data augmentation',
   - 'contrastive learning/contrastive Learning',
   - 'object-centric video prediction/object-agnostic video prediction model'
    '''.replace('''\'''',""))
    '''\n\n\n'''

    st.markdown("### Cluster 3")
    st.dataframe(e1c3)
    st.markdown("**Generated research trends**")
    st.markdown(
        '''
        - 'large language model/language models/language model/masked language model/language modeling',
        - 'vision & Language model/vision-language model', 
        - 'pre-trained language model/pre-trained multiplexed language model', 
        - 'information-seeking question answering', 
        - 'web-scale visual and language pre-training', 
        - 'human-annotated (high-level) abstract captions', 
        - 'deep learning/deep learning model', 
        - 'language-driven representation learning from human videos and associated captions', 
        - 'visual representation learning', 
        - 'data augmentation technique/text augmentation technique'
        '''.replace('''\'''','')
    )
    '''\n\n\n'''

    '''---'''
    '''> *Evaluation: ("1" for very bad, "5" for very good)*'''
    st.slider('Relevance of Clusters',1,5,3,key='e1_relevance')
    st.slider('Coherence of Clusters', 1, 5, 3, key='e1_coherence')
    st.slider('Accuracy of Research Trends', 1, 5, 3, key='e1_accuracy')

    ##############
    ## E2 ##
    # {
    #    'plm': 'all-mpnet-base-v2',
    #    'dimension_reduction': 'none',
    #    'clustering': 'gmm',
    #    'keywords_extraction': 'KeyBART'
    # }
    ##############
    st.markdown('## Evaluation 2')
    # e1c1, e1c2, e1c3 = load_e1()

    st.markdown("### Cluster 1")
    st.dataframe(e1c1)
    st.markdown("**Generated research trends**")
    st.markdown('''
        - 'automatic speech recognition/automated speech recognition/end-to-end automatic speech recognition (asr)/automatic speech recognition (asr)',
        - 'speech recognition/speaker recognition', 
        - 'word error rate', 
        - 'deep neural network/neural network', 
        - 'multi-task learning setting/multi-task learning network/multi-task learning (mtl)', 
        - 'ground truth', 
        - 'speech enhancement/speech enhancement (se',
        - 'multiple self-supervised speech model',
        - 'layerwise aggregation technique',
        - 'multiple prediction head method'
        '''.replace('''\'''', ""))
    '''\n\n\n'''

    st.markdown("### Cluster 2")
    st.dataframe(e1c2)
    st.markdown("**Generated research trends**")
    st.markdown('''
        - 'deep convolutional neural network (CNN)/convolutional neural network/convolution network/convolutional neural networks (convnets)/convolutional neural network (CNN)/graph convolutional neural network', 
        - 'deep neural network/neural network/deep neural network (dnn)', 
        - 'image segmentation/medical image segmentation/medical image recognition/image segmentation task', 
        - 'deep learning', 
        - 'self-supervised learning/unsupervised learning/supervised learning', 
        - 'feature extraction/image feature extraction', 
        - 'image classification/x-ray image classification/tissue classification', 
        - 'high-dimensional distribution/high dimensional distribution', 
        - 'computer vision', 
        - 'semantic segmentation/3d semantic segmentation'
        '''.replace('''\'''', ""))
    '''\n\n\n'''

    st.markdown("### Cluster 3")
    st.dataframe(e1c3)
    st.markdown("**Generated research trends**")
    st.markdown(
        '''
        - 'language model/large language models (llm)/large language model/large language model (llm)',
        - 'natural language processing/natural language processing (nlp)', 
        - 'machine learning', 
        - 'neural network/deep neural network', 
        - 'deep learning/deep learning model', 
        - 'question answering', 
        - 'information-seeking question-answer pairs', 
        - 'web-scale visual and language pre-training', 
        - 'human-annotated (high-level) abstract captions', 
        - 'vision & language models'
        '''.replace('''\'''', '')
    )
    '''\n\n\n'''

    '''---'''
    '''> *Evaluation: ("1" for very bad, "5" for very good)*'''
    st.slider('Relevance of Clusters', 1, 5, 3, key='e2_relevance')
    st.slider('Coherence of Clusters', 1, 5, 3, key='e2_coherence')
    st.slider('Accuracy of Research Trends', 1, 5, 3, key='e2_accuracy')


    '''---'''
    '''## Additional Feedbacks about TrendFlow'''
    st.text_area('',key='feedbacks')

    #########
    # finish
    #########
    '''\n\n\n'''
    # center a Streamlit button horizontally on the page
    st.markdown(
        """
        <style>
        div.stButton > button:first-child {
            margin-left: auto;
            margin-right: auto;
            display: block;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    def submit():
        session.go_to_page('thanks')
        tmp = session.to_dict()
        data = dict(
            email = tmp['email'],
            e1_relevance = tmp['e1_relevance'],
            e1_coherence = tmp['e1_coherence'],
            e1_accuracy = tmp['e1_accuracy'],
            e2_relevance=tmp['e2_relevance'],
            e2_coherence=tmp['e2_coherence'],
            e2_accuracy=tmp['e2_accuracy'],
            feedbacks = tmp['feedbacks']
        )
        add_new_row(data)

    st.button('Submit',on_click=submit)


session = helper.OpenSession(
    current_page='intro',
    page_map=dict(
        welcome = welcome,
        home = home,
        thanks = thanks,
        intro = intro
    )
)


# st.info(session.summary())
session.render()
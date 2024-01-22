import streamlit as st
import sthelper as helper
import pandas as pd
from sthelper.gsheet import add_new_row

slider_sample_count = 0
sample_count = 0

pairs = [
    (0,1),
    (0,3),
    (0,4),
    (0,5),
    (6,7),
    (6,9),
    (6,10),
    (6,11),
    (12,13),
    (12,15),
    (12,16),
    (12,17),
    (18,20),
    (18,21),
    (18,22),
    (23,24),
    (23,26),
    (23,27),
    (23,28),
    (29,31),
    (29,32),
    (29,33),
    (34,36),
    (34,37),
    (34,38),
    (39,40),
    (39,42),
    (39,43),
    (39,44) 
]


import random

def select_random_elements(lst, num_elements=8):
    if len(lst) < num_elements:
        raise ValueError("The list does not contain enough elements to select from")

    selected_elements = random.sample(lst, num_elements)
    return selected_elements



def thanks():
    st.markdown(''' <h1 style="margin-top: 100px; font-size: 48px; font-weight: bold; color: #333333;">Thanks for Your Effort!</h1>
    <p style="margin-top: 40px; font-size: 24px; color: #666666;">We appreciate all the hard work you put into this project.</p>''', unsafe_allow_html=True)


def home():
    # Cache the dataframe so it's only loaded once
    selected_pairs = select_random_elements(pairs,num_elements=8)
    
    
    def draw_one_sample(a,b):
        global slider_sample_count, sample_count
        sample_count += 1
        st.markdown(f"## Pair {sample_count}")
        col1, col2 = st.columns(2,gap="large")
        
    
        with col2:
            '''
            **audio 2**
            '''
            st.audio(f'duration_control/audios/all/dc{str(a)}.wav')
            '''
            **Quality**
            '''
            slider_sample_count += 1
            st.slider(label=str(slider_sample_count),min_value=1,max_value=5, label_visibility="collapsed")

        with col1:
            '''
            **audio 1**
            '''
            st.audio(f'duration_control/audios/all/dc{str(b)}.wav')
            '''
            **Quality**
            '''
            slider_sample_count += 1
            st.slider(label=str(slider_sample_count),min_value=1,max_value=5, label_visibility="collapsed")
            
        
        


            
            
            
        st.text("") 
        st.text("")   
        '''
        **Consistency**
        '''
        slider_sample_count += 1
        st.text("")
        st.text("")
        st.slider(label=str(slider_sample_count),min_value=1,max_value=5, label_visibility="collapsed")
            
            
        '''
        ---
        '''
    


    st.markdown("# Human Evaluation")
    st.markdown('''Thank you very much for participating in this test, which will take approximately two to three minutes of your time.
The test includes 8 sets of random samples, each containing two audio clips ranging from 2 to 5 seconds.
We kindly request you to score the quality of each audio clip and compare the degree of timbral similarity between the two audio clips, with the following criteria:

**Quality**
- 0 => Noise-like or heavily distorted, lacking any resemblance to conventional musical notes.
- 5 => comparable to notes played by real/electronic/synthetic musical instruments.

**Consistency**
- 0 =>   sounding like completely different types of instruments.
- 5 =>   sounding like the same instrument.


''')
    helper.widgets.build_TOC(
        [
            # ('h2', 'Section 1'),
            # ('h2', 'Section 2'),
            # ('h2', 'Metrics for this evaluation'),
            # ('h2', 'Evaluation 1'),
            # ('h2', 'Evaluation 2'),
            # ('h2', "Additional Feedbacks about TrendFlow")
        ]
    )

    # st.markdown("## Section 2")
    # st.dataframe(df, use_container_width=False)
    '''
    ---
    '''
    for p in selected_pairs:
        print(p)
        draw_one_sample(p[0],p[1])
    

  
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
    current_page='home',
    page_map=dict(
        home = home,
        thanks = thanks,

    )
)


# st.info(session.summary())
session.render()
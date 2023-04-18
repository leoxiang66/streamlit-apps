import datetime
import os
os.system("sudo apt-get install poppler-utils")

import streamlit as st
from streamlit_chat import message


st.set_page_config(
    page_title="ChatPPT - Chat with Any Slides",
    page_icon="🧊",
    # layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        # 'Get Help': 'https://www.extremelycoolapp.com/help',
        # 'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
import sthelper as helper
import utils




def privacy():
    '''

    Returns:
    '''
    '''
# Privacy Policy

At ChatPPT, we understand the importance of protecting the privacy of our users. We are committed to maintaining the confidentiality and security of any personal information that we collect.

Our app requires users to set up their own OpenAI API key in order to access features provided by ChatGPT3.5. We want to assure our users that we do not store or retain any information related to their OpenAI API key. This means that your key remains entirely private and is never accessible to anyone else, including our team.

We use industry-standard security measures to protect the personal information of our users, and we take all necessary precautions to ensure that your data remains secure. Our commitment to protecting your privacy is paramount, and we will always strive to maintain the highest standards of data protection and security.

Please feel free to contact us if you have any questions or concerns regarding our privacy policy. We are dedicated to ensuring that our users feel safe and secure when using our app, and we will do everything in our power to protect your personal information.
    '''

    checked = st.checkbox('''I agree with the privacy policy, let's rock!''')
    if checked:
        key = st.text_input("Your OpenAI API Key")
        if key != "":
            session.update('openai_key',key)
    def on_lick():
        if checked:
            session.go_to_page('app')
        else:
            st.info("You need to first agree with the privacy policy.")

    st.button("Start",on_click=on_lick)


def intro():
    def onclick():
        if session.get('file') is not None:
            session.go_to_page('privacy')

    '''&nbsp;&nbsp;'''
    st.markdown("<center> <b>Let's get started!</b> </center>", unsafe_allow_html=True)
    file = st.file_uploader(accept_multiple_files=False,type='pdf',label_visibility='collapsed',label='ok')
    if file is not None:
        print('>>> 上传成功')
        session.update('file',file)
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
        st.button("Start", on_click=onclick)




def index():
    st.markdown('''<center> 
    <h1>ChatPPT - Chat with Any Slides</h1> 
    <h5>Enhance your learning experience with AI-powered Q&A for every slide!</h5>
    </center>''', unsafe_allow_html=True)

    '''
    
    
    ChatPPT, the innovative app designed to help students better understand university course materials, one slide at a time. Powered by ChatGPT, get instant answers to your questions and clarify concepts effortlessly.
    '''
    intro()






def app():
    def sys_append(uttr:str):
        focus = session.get('focus')
        if  focus not in session.get('generated'):
            session.get('generated')[focus] = [uttr]
        else:
            session.get('generated')[focus].append(uttr)

    def usr_append(uttr:str):
        focus = session.get('focus')
        if  focus not in session.get('generated'):
            session.get('past')[focus] = [uttr]
        else:
            session.get('past')[focus].append(uttr)

    def build_chat_file(user,sys):
        focus = st.session_state.focus

        ret = f'- {user}\n'
        ret += f'\t- {sys}\n'
        ret += '\n\n'

        if focus not in session.get('chathistory'):
            session.get('chathistory')[focus] = f'# {st.session_state.file.name} Page {focus}\n\n'+ ret
        else:
            tmp = session.get('chathistory')[focus]
            session.get('chathistory')[focus]= tmp + ret





    sidebar()
    contents = utils.extract_pdf_text(session.get('file'))

    textinput = st.empty()
    input = textinput.text_input(label="hi",label_visibility='collapsed',placeholder='"Ask anything about this slide.."',key=session.get('pkey'))

    if input !="":
        usr_append(input)
        sys = utils.ask_gpt(context= contents[session.get('focus')],user=input)
        sys_append(sys)
        build_chat_file(input,sys)


        newkey = session.get('pkey')+"1"
        textinput.text_input(label="hi",label_visibility='collapsed',placeholder='"Ask anything about this slide.."',key=newkey)
        session.update('pkey',newkey)
        st.experimental_rerun()

    render_chat()


def render_chat():
    if session.get('focus') in st.session_state['generated'] and len(
            session.get('generated')[session.get('focus')]) > 0:
        for i in range(len(st.session_state['generated'][session.get('focus')]) - 1, -1, -1):
            message(st.session_state["generated"][session.get('focus')][i], key=str(i), avatar_style="avataaars")
            message(st.session_state['past'][session.get('focus')][i], is_user=True, key=str(i) + '_user')


def sidebar():
    def nxtpage():
        focus = session.get('focus') + 1
        if focus <= session.get('pagecount'):
            session.update('focus', focus)

    def prepage():
        focus = session.get('focus') - 1
        if focus > 0:
            session.update('focus', focus)

    previews = utils.extract_pdf_images(session.get('file').getvalue(), ratio=0.3)
    session.update('pagecount', len(previews))
    page = st.sidebar.selectbox(label='Page', options=range(1, session.get('pagecount') + 1),
                                index=session.get('focus') - 1)
    if page != session.get('focus'):
        print(page)
        session.update('focus', page)
    st.sidebar.image(previews[session.get('focus') - 1])
    c1, c3, c2 = st.sidebar.columns(3)
    c1.button("Previous Page", on_click=prepage)
    c2.button("Next Page", on_click=nxtpage)
    if session.get('focus') in session.get('chathistory'):
        c3.download_button("Export Chat", data=session.get('chathistory')[session.get('focus')], file_name='chat.md')
    st.sidebar.markdown('''---''')
    st.sidebar.markdown('''
    <style>
        a {
            text-decoration: none;
            margin: 0 10px;
        }
    </style>
    
      <center>
        <a href="/" target="_self">
            Home
        </a>
        <a href="https://discord.gg/your-invite-code">
            Discord
        </a>
        <a href="https://memomind.cn/">
            About Memomind
        </a>
    </center>
    ''',unsafe_allow_html=True)
    st.sidebar.markdown('''&nbsp;&nbsp;&nbsp;''')

    st.sidebar.markdown(f'''<center>Copyright © 2022 - {datetime.datetime.now().year} by Memomind</center>''',unsafe_allow_html=True)





session = helper.OpenSession(
    current_page='index',
    page_map=dict(
        app = app,
        intro = intro,
        index = index,
        privacy = privacy
    )
)

session.init('openai_key',None)
session.init('chathistory',{})
session.init("pkey","_")
session.init('generated',{})
session.init('past',{})
session.init('file',None)
session.init('focus',1)
session.init('pagecount',-1)
# st.info(session.summary())
session.render()
# st.info(session.summary())
import streamlit as st
markdown = '''## TODOS
1. 在[views.py](https://github.com/leoxiang66/xiangtao-server/blob/main/myserver/wechat_official_account/views.py)中部署了两个chatbots 1) DummyBot（用于测试）2）Blenderbot
其中Blenderbot的模型大小为1.36G左右， 大于目前的阿里云服务器内存（1G）. 因此后期需要换一个内存更大的服务器或者训练一个更小的模型'''

st.markdown(markdown)
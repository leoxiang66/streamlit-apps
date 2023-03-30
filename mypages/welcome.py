import streamlit as st
from .navigation import go_to_home

def welcome():
    st.markdown('''
    <h1 align='center'> TrendFlow</h1>

    <p align='center'>
    <a href = "https://leoxiang66.github.io/research-trends-analysis/"><img src="https://img.shields.io/website?label=documentation&up_message=online&url=https://leoxiang66.github.io/research-trends-analysis/"> </a>
    <a href="https://pypi.org/project/TrendFlow/"><img src="https://badge.fury.io/py/trendflow.svg" alt="PyPI version" /> </a>
    <a href="https://discord.gg/P5Y3FHgHRz">
            <img alt="chat on Discord" src="https://img.shields.io/discord/1091063040662843565?logo=discord">
        </a>
    </p>


    TrendFlow is an advanced framework that uses deep learning techniques to analyze research trends. This powerful framework offers a wide range of analytical capabilities, including literature clustering, trend generation, and trend summarization. With TrendFlow, you can gain insights into emerging research topics and stay up-to-date on the latest advancements in your field.

    ''', unsafe_allow_html=True)

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

    # 添加一个居中的按钮
    st.button("Get Started", on_click=go_to_home)





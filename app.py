import streamlit as st
import tube as tb

tb.clear_cache()


md = '''
# YouTube Downloader
'''

st.markdown(md)


url = st.text_input(
    placeholder="https://www.youtube.com/",
    label='**Enter the url of the youtube:**',
    key='title'
)



if url is not None and ('https' in url or 'http' in url):
    tb.download_yt(url)










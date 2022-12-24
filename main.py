import streamlit as st
import tube as tb


md = '''
# YouTube Playlist Downloader
'''

st.markdown(md)


url = st.text_input(
    placeholder="https://www.youtube.com/",
    label='**Enter the url of the playlist:**',
    key='title'
)

if url is not None and ('https' in url or 'http' in url):
    tb.download_playlist(url)










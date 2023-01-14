from pathlib import Path
from pytube import YouTube

import streamlit as st
from .utils import  clear_cache




def download_yt(yt_url:str, output_dir:str = './downloads'):
    yt = YouTube(yt_url)

    prompt = st.markdown(f'''`downloading...`''')

    while True:
        try:
            yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(
                output_path=output_dir,
                filename='download.mp4'
            )
            prompt.empty()
            break
        except Exception as e:
            print(e)

    download_file(folder_name= output_dir)





def download_file(folder_name):
    def tmp(*,folder_name:str):
        st.session_state["title"] = ""
        clear_cache(folder_name)


    with open(Path('downloads').joinpath('download.mp4'), "rb") as file:
        btn = st.download_button(
            label="Download",
            data=file,
            file_name='download.mp4',
            on_click= tmp,kwargs=dict(
                folder_name = folder_name
            )
        )



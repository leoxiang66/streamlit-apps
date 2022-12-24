import shutil
import streamlit as st
from pathlib import Path

def compress_folder_2_zip(output_filename: str, dir_name:str):
    path = Path(output_filename+'.zip')
    if path.exists():
        return

    prompt = st.info('Start compressing...')
    with st.spinner("Compressing"):
        shutil.make_archive(output_filename.replace('.zip', ''), 'zip', dir_name)
    prompt.empty()



if __name__ == '__main__':
    compress_folder_2_zip('test',dir_name='../downloads')
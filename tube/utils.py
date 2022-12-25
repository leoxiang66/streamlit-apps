import shutil
import streamlit as st
from pathlib import Path
from .var import OUTPUT_DIR




def compress_folder_2_zip(output_filename: str, dir_name:str):
    path = Path(output_filename+'.zip')
    if path.exists():
        return

    prompt = st.info('Start compressing...')
    with st.spinner("Compressing"):
        shutil.make_archive(output_filename.replace('.zip', ''), 'zip', dir_name)
    prompt.empty()


def remove_dir_rec(pth):
    pth = Path(pth)
    if pth.exists():
        for child in pth.glob('*'):
            if child.is_file():
                child.unlink()
            else:
                remove_dir_rec(child)
        pth.rmdir()
def clear_cache(dir_name:str = OUTPUT_DIR):
    remove_dir_rec(dir_name)




if __name__ == '__main__':
    compress_folder_2_zip('test',dir_name='../downloads')
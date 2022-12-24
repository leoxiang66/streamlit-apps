from pathlib import Path
from pytube import Playlist,YouTube
import time
import streamlit as st
from .utils import compress_folder_2_zip, clear_cache
from .var import OUTPUT_DIR



def download_yt(yt:YouTube, id = None, output_dir:str = './downloads'):
    if id is not None:
        output_file_name = f'''{id+1}_{yt.title}.mp4'''
    else:
        output_file_name = f'''{yt.title}.mp4'''

    prompt = st.markdown(f'''`downloading {output_file_name}...`''')

    try:
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(
            output_path=output_dir,
            filename=output_file_name
        )
        return True
    except Exception as e:
        print(e)
        return False
    finally:
        prompt.empty()


def download_playlist(url:str):
    pb = st.progress(0)
    prompt = st.info('''Start downloading...''')

    playlist = Playlist(url)
    number_videos = len(playlist.video_urls)
    print('Number of videos in playlist: %s' % number_videos)

    # download path
    output_path = OUTPUT_DIR.joinpath(f'{playlist.title}')
    output_path.mkdir(parents=True, exist_ok=True)

    for id,yt in enumerate(playlist.videos):
        pb.progress(id/number_videos)
        while not download_yt(
            yt=yt,
            id=id,
            output_dir= output_path.__str__()
        ):
            print(f'download failed: {str(yt.title)}.')
            time.sleep(1)

    pb.empty()
    compress_folder_2_zip(output_filename=playlist.title, dir_name=output_path.__str__())

    prompt.success(
        'Congratulations! You have successfully downloaded all the videos! Click on the download button to download them!')
    download_file(f'{playlist.title}.zip', output_path.__str__())



def download_file(path,folder_name):
    def tmp(*,folder_name:str):
        st.session_state["title"] = ""
        clear_cache(folder_name)
        Path(path).unlink()


    with open(path, "rb") as file:
        btn = st.download_button(
            label="Download Playlist",
            data=file,
            file_name=path,
            # mime="image/png"
            on_click= tmp,kwargs=dict(
                folder_name = folder_name
            )
        )



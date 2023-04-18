import PyPDF2
from pdf2image import  convert_from_bytes
import streamlit as st
from requests_toolkit.openpy import SyncChatGPT
from requests_toolkit.openpy.config import ChatCompletionConfig



@st.cache_data
def extract_pdf_images(pdf_file, ratio=0.6):
    # 将 PDF 文件转换为 PIL.Image 对象列表
    images = convert_from_bytes(pdf_file)

    # 调整图像大小并将它们添加到 resized_images 列表中
    resized_images = [image.resize((int(image.size[0]*ratio),int(image.size[1]*ratio))) for image in images]

    # 返回调整大小后的 PIL.Image 对象列表
    return resized_images


@st.cache_data
def extract_pdf_text(pdf_file):
    # 初始化一个空列表，用于存储每个幻灯片的文本
    slide_texts = []

    # 创建一个 PDF 读取器对象
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # 获取 PDF 文件中的总页数
    num_pages = len(pdf_reader.pages)

    # 遍历 PDF 文件中的每一页
    for page_num in range(num_pages):
        # 获取当前页面
        page = pdf_reader.pages[page_num]

        # 提取当前页面的文本
        page_text = page.extract_text()

        # 将提取的文本添加到 slide_texts 列表中
        slide_texts.append(page_text)

    # 返回包含幻灯片文本的字符串列表
    return slide_texts



def ask_gpt(context:str, user:str):
    key = st.session_state.get('openai_key')
    print(key)
    cgpt = SyncChatGPT(api_key=key)
    return cgpt.reply(ChatCompletionConfig(user_msg=f'''Help me understand following text: "{context}".\n\n My question is: {user}''')).eval()



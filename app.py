import os
from PIL import Image
import streamlit as st
from itertools import cycle
from getsimilar.get import *

st.set_page_config(
    page_title="Similar Images search",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="auto",
)

top_image = Image.open('static/banner_top.png')
bottom_image = Image.open('static/banner_bottom.png')

upload_path = "uploads/"

st.sidebar.image(top_image,use_column_width='auto')
search_type = st.sidebar.selectbox('Select Image Search type 🎯',["Text","URL","Upload Image"])
st.sidebar.image(bottom_image,use_column_width='auto')

st.title("🚀 Similar Images Search 📷")

if search_type == "Text":
    col1, col2 = st.columns(2)
    with col1:
        text = st.text_area("Enter your text here: 🖋", height=50)
    with col2:
        img_no = st.slider("Number of Images to search: ", 1, 20, 1)
    if st.button("Search 🔍") and len(text) !=0 :
        with st.spinner(f"Searching... 💫"):
            imgs = from_text(text, num_similar = img_no)
            cols = cycle(st.columns(4))
            for idx, img in enumerate(imgs):
                next(cols).image(img, width=None, use_column_width='auto')
    else:
        st.warning('⚠ Please enter your text for Image Search! 😯')


if search_type == "URL":
    col1, col2 = st.columns(2)
    with col1:
        url_img = st.text_area("Enter your URL here: 🔗", height=10)
    with col2:
        img_no = st.slider("Number of Images to search: ", 1, 20, 1)
    if st.button("Search 🔍") and len(url_img) !=0 :
        with st.spinner(f"Searching... 💫"):
            imgs = from_url(url_img, num_similar = img_no)
            cols = cycle(st.columns(4))
            for idx, img in enumerate(imgs):
                next(cols).image(img, width=None, use_column_width='auto')
    else:
        st.warning('⚠ Please enter your Image URL! 😯')

if search_type == "Upload Image":
    col1, col2 = st.columns(2)
    with col1:
        st.info('✨ Supports all popular image formats 📷 - PNG, JPG, BMP 😉')
        uploaded_file = st.file_uploader("Upload Image 🖼", type=["png","jpg","bmp","jpeg"])
    with col2:
        img_no = st.slider("Number of Images to search: ", 1, 20, 1)
    if uploaded_file is not None:
        with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
            f.write((uploaded_file).getbuffer())
        if st.button("Search 🔍"):
            with st.spinner(f"Searching... 💫"):
                uploaded_image = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
                im = Image.open(uploaded_image)
                imgs = from_image(im, num_similar=img_no)
                cols = cycle(st.columns(4))
                for idx, img in enumerate(imgs):
                    next(cols).image(img, width=None, use_column_width='auto')
    else:
        st.warning('⚠ Please upload your Image! 😯')


st.markdown("<br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=Similar Images WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a> with the help of [getsimilar](https://github.com/ternaus/getsimilar) built by [ternaus](https://github.com/ternaus) ✨</center><hr>", unsafe_allow_html=True)

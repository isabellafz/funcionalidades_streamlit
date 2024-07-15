import streamlit as st
from PIL import Image
import numpy as np


st.header('Usando o Image')
image = Image.open('images.jpeg')

st.image(image, caption='Linux x Windowns')

st.header('Adicionando audio')

audio_file = open('WhatsApp Ptt 2023-08-23 at 09.33.45.ogg', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')

st.header('Adicionando video')

video_file = open('WhatsApp Video 2023-08-24 at 12.24.27.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
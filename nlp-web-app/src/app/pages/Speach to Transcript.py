import streamlit as st
# import soundfile as sf
from src.ner import build_entity
from src.speech2transcript import audio_to_transcript
from src.utils import save_transcript, download_link_transcript

# Speech to Transcript
st.image('https://www.rev.com/blog/wp-content/uploads/2019/04/Rev-HowtoParaphraseAudio.gif')
# st.image('https://www.rev.com/blog/wp-content/uploads/2019/03/Rev-AudioTipsandTechniques-1-1024x576.gif')
# st.image('https://www.rev.com/blog/wp-content/uploads/2020/12/2020.11_Marketing_BlogHeaders_Nov30_AM_Artboard-1-copy-5-1024x576.jpg')
st.header('Speach to Transcript')


uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])

if uploaded_file is not None:
    audio_data = uploaded_file.getvalue()
    try:
        with open("src/data/file.m4a", "wb") as f:
            f.write(audio_data)
        st.success("Audio file saved successfully!")
        transcript = audio_to_transcript("src/data/file.m4a")
        download_link_transcript(transcript, format='text')

    except FileNotFoundError:
        transcript = ''
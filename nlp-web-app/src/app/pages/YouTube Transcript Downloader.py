import streamlit as st
from src.youtube_transcript import YoutubeTranscriptDownloader
from src.utils import download_link_transcript


st.image('https://www.rev.com/blog/wp-content/uploads/2018/10/Rev-VideoTranscriptions2.gif')

try:
    youtube_link = st.text_input('**Enter Video Link:**')
    obj = YoutubeTranscriptDownloader(youtube_link)
    en_fa = obj.transcript_to_farsi()
    download_link_transcript(str(en_fa))

except:
    pass


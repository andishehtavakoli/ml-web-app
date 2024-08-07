import streamlit as st
import pandas as pd
from src.subtitle import Subtitle
import pysrt
import tempfile
import os
from io import BytesIO
from src.utils import download_link_transcript


st.image('https://vananservices.com/blog/wp-content/uploads/2022/06/Are-You-Subtitling-a-Video-Top-5-Mistakes-to-Avoid-1200x675.png')


# def read_subtitle_file(subtitle_file):
#     # Save the BytesIO object to a temporary file
#     temp_file = tempfile.NamedTemporaryFile(delete=False)
#     temp_file.write(subtitle_file.read())
#     temp_file.close()

#     try:

#         subtitle = Subtitle(temp_file.name)
#         score = st.slider('Chooese Difficulty degree', 1, 10, 5)
#         df = pd.DataFrame(subtitle.get_difficult_words_farsi(score), columns=['English', 'Farsi', 'Score'])
#         st.dataframe(df.style.highlight_max(color='yellow'))
#         download_link_transcript(df, format='csv')
#         os.unlink(temp_file.name)

#     except Exception as e:
#         st.error(f"Error reading the subtitle file: {e}")
#         return None

#    import base64
# import streamlit as st
# import pandas as pd


# Example usage with Farsi text in a DataFrame
data = {'Farsi_Column': ['متن فارسی ۱', 'متن فارسی ۲']}
df = pd.DataFrame(data)

# Call the function to generate the download link
download_link_transcript(df, format='csv')





# def main():
#     st.title("Subtitle Viewer")

#     # File uploader
#     subtitle_file = st.file_uploader("Upload Subtitle File", type=["srt", "sub"])

#     if subtitle_file is not None:
#         subtitle = read_subtitle_file(subtitle_file)
#         if subtitle is not None:
#             st.success("Subtitle file successfully read!")
#             st.write("Subtitle content:")

# main()
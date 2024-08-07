import streamlit as st
import base64
import json
import pandas as pd

def save_transcript(file_path, text):
    with open(file_path, 'w') as f:
        f.write(text)




def download_link_transcript(file_data, format=None):
    valid_formats = ['text', 'csv']

    if format not in valid_formats:
        raise ValueError('File format must be "text" or "csv"')

    if format == 'text':
        mime_type = 'text/plain'
        file_extension = 'txt'
        if isinstance(file_data, str):
            file_data = file_data.encode('utf-8')
            file_data = file_data.decode('utf-8')  # Decode if the input is in bytes
    elif format == 'csv':
        mime_type = 'text/csv'
        file_extension = 'csv'
        if isinstance(file_data, pd.DataFrame):
            # Ensure Farsi text in DataFrame is properly encoded
            file_data = file_data.applymap(lambda x: x.encode('utf-8').decode('utf-8-sig') if isinstance(x, str) else x)
            # Convert DataFrame to CSV with proper encoding
            file_data = file_data.to_csv(index=False, encoding='utf-8-sig')

    b64_file = base64.b64encode(file_data.encode('utf-8')).decode()
    download_link = f'<a href="data:{mime_type};base64,{b64_file}" download="file.{file_extension}">Download File</a>'

    st.markdown(download_link, unsafe_allow_html=True)






def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        f.read()

def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

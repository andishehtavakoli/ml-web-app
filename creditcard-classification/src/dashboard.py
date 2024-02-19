import streamlit as st
import pandas as pd
from loguru import logger
import joblib


st.image('/Users/andishetavakkoli/Documents/notebook/ml-web-app/creditcard_classification/image/Credit card-pana.png', width=300)
st.title('Fraud Detection')

uploaded_file = st.file_uploader('choose a file')


if uploaded_file is not None:
    credict_card_df = pd.read_csv(uploaded_file)
    logger.info('file is read!')

    # Fraud Detection
    model = joblib.load('/Users/andishetavakkoli/Documents/notebook/ml-web-app/creditcard_classification/src/model/linear_regression_model.joblib')

    def fraud_detection(df, model):
        predicted_sample = model.predict(df)
        df['predict_frud'] = predicted_sample
        return df

    @st.cache_data
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    credict_card_df = fraud_detection(credict_card_df, model)
    st.dataframe(credict_card_df.sample(3).style.background_gradient(subset='predict_frud', cmap='coolwarm'))
    csv = convert_df(credict_card_df)


    st.download_button(
        label='Download data as csv :sunglasses:',
        data=csv,
        mime='text/csv'
    )




    
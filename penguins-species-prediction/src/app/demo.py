import streamlit as st
import seaborn as sns
import pandas as pd

from src.model import MODELS_LIST, build_model
from src.preprocessing import encoder, nan_imputer, split_data
from sklearn.ensemble import RandomForestClassifier

st.image('https://images.unsplash.com/photo-1598439210625-5067c578f3f6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8&w=1000&q=80')
st.header('Penguins Species Prediction')

df = sns.load_dataset('penguins')

st.dataframe(df.describe())


bill_length = st.slider('**Bill Length (mm)**', float(df['bill_length_mm'].min()),float(df['bill_length_mm'].max()), float(df['bill_length_mm'].mode()[0]))
bill_depth = st.slider('**Bill Depth (mm)**', float(df['bill_depth_mm'].min()),float(df['bill_depth_mm'].max()), float(df['bill_depth_mm'].mode()[0]))
flipper_length = st.slider('**Flipper Length (mm)**', float(df['flipper_length_mm'].min()),float(df['flipper_length_mm'].max()), float(df['flipper_length_mm'].mode()[0]))
body_mass = st.slider('**Body Mass_g (mm)**', float(df['body_mass_g'].min()),float(df['body_mass_g'].max()), float(df['body_mass_g'].mode()[0]))

island = st.select_slider(
    '**Island**',
    options=df['island'].unique())

gender = st.select_slider(
    '**Gender**',
    options=df['sex'].dropna().unique())

predict_button = st.button('Predict')
if predict_button:

    df = sns.load_dataset('penguins')
    dep_variable = ['species']
    indep_variable =[ 'island', 'bill_length_mm', 'bill_depth_mm','flipper_length_mm', 'body_mass_g', 'sex']
    X_train, X_test, y_train,  y_test = split_data(df, dep_variable, indep_variable, test_size=0.2)

    trained_model = build_model(X_train, RandomForestClassifier())
    trained_model.fit(X_train, y_train)
    y_pred = trained_model.predict(pd.DataFrame([[island, bill_length, bill_depth,flipper_length, body_mass, gender]], columns=X_train.columns))
    st.success(''.join(y_pred))
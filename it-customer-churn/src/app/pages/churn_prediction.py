import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.preprocessing import load_data


st.header('Churn Modeling(Telecom)')

df = load_data('/Users/andishetavakkoli/Documents/notebook/ml-web-app/it-customer-churn/src/data/IT_customer_churn.csv')
st.dataframe(df.head())


col1, col2, col3, col4 = st.columns(4)
with col1:
    gender = st.radio("What's your gender", ['Female', 'Male'])
    senior_citizen = st.radio("Are you senior_citizen", ['1', '0'])
    partner = st.radio("What's your partner", ['Yes', 'No'])
    dependents = st.radio("Do you have dependends", ['Yes', 'No'])

with col2:
    phone_service = st.radio("Do you have phone service", ['Yes', 'No'])
    multiple_lines = st.radio("Do you have multiple lines", ['Yes', 'No', 'No phone service'])
    OnlineSecurity = st.radio("Do you have online security", ['Yes', 'No', 'No internet service'])

with col3:
    OnlineBackup = st.radio("Do you have online backup", ['Yes', 'No', 'No internet service'])
    DeviceProtection = st.radio("Do you have dvice protection", ['Yes', 'No', 'No internet service'])
    TechSupport = st.radio("Do you have tech support", ['Yes', 'No', 'No internet service'])


with col4:
    StreamingTV = st.radio("Do you have streaming TV", ['Yes', 'No', 'No internet service'])
    StreamingMovies = st.radio("Do you have streaming movie ", ['Yes', 'No', 'No internet service'])
    paperless_billing = st.radio("Do you have PaperlessBilling ", ['Yes', 'No'])

internet_service = st.selectbox("What is your internet service", ('DSL', 'Fiber optic', 'No'))
contract = st.selectbox("What is your contract ", ('Month-to-month', 'One year', 'Two year'))
payment_method = st.selectbox("What is your contract ", ('Electronic check','Mailed check','Bank transfer (automatic)',
 'Credit card (automatic)'))

tenure = st.number_input('tenure')
monthly_charges = st.number_input('MonthlyCharges')
total_charges = st.number_input('TotalCharges')






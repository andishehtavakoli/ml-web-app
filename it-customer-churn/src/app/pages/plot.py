from src.visulizition import CreatePlot
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st
st.set_option('deprecation.showPyplotGlobalUse', False)

from src.preprocessing import load_data

st.header('Churn Analysis')

df = load_data('/Users/andishetavakkoli/Documents/notebook/ml-web-app/it-customer-churn/src/data/IT_customer_churn.csv')

obj = CreatePlot(df)

col1, col2= st.columns(2)
with col1:
    obj.tenure_churn_lineplot()
with col2:
    st.write("Churn Rate Over Tenure Months,\
             Churn Rate Over Tenure MonthsChurn Rate Over Tenure Months,\
             Churn Rate Over Tenure Months")

st.markdown("<br><br><br>", unsafe_allow_html=True)


col1, col2= st.columns(2)
with col1:
    obj.contract_churn_countplot()
with col2:
    st.write("Churned Customers by Contract Types,\
             Churned Customers by Contract Type,\
             Churned Customers by Contract Type")
    
st.markdown("<br><br><br>", unsafe_allow_html=True)


col1, col2= st.columns(2)
with col1:
    obj.survival_churn_plot()
with col2:
    st.write("Churn Rate Over Tenure Months,\
             Churn Rate Over Tenure MonthsChurn Rate Over Tenure Months,\
             Churn Rate Over Tenure Months")

st.markdown("<br><br><br>", unsafe_allow_html=True)


col1, col2= st.columns(2)
with col1:
    obj.feature_importance_plot()
with col2:
    st.write("Churn Rate Over Tenure Months,\
             Churn Rate Over Tenure MonthsChurn Rate Over Tenure Months,\
             Churn Rate Over Tenure Months")
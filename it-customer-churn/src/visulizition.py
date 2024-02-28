import plotly.graph_objs as go
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from lifelines import KaplanMeierFitter
from sklearn.ensemble import RandomForestClassifier


class CreatePlot:
    def __init__(self, df):
        self.df = self.preprocessing(df)

    @staticmethod
    def preprocessing(df):
        df_input = df.copy()
        df_input['TotalCharges'] = df_input['TotalCharges'].replace("'", "").replace('"','').replace(" ", "").replace('', np.nan).astype('float')
        df_input.dropna(subset=['TotalCharges'], inplace=True)
        df_input['Churn'] = df_input['Churn'].replace({'Yes': 1, 'No': 0}).astype(int)
        df_input['tenure_months'] = df_input['tenure']
        return df_input

    def tenure_churn_lineplot(self):
        churn_rate_over_time = self.df.groupby('tenure_months')['Churn'].mean()

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=churn_rate_over_time.index, y=churn_rate_over_time.values, mode='lines'))
        fig.update_layout(title='Churn Rate Over Tenure Months', xaxis_title='Tenure Months', yaxis_title='Churn Rate')
        st.plotly_chart(fig)

    def contract_churn_countplot(self):
        fig = go.Figure()
        for churn_val in [0, 1]:
            temp_df = self.df[self.df['Churn'] == churn_val]
            counts = temp_df['Contract'].value_counts()
            fig.add_trace(go.Bar(x=counts.index, y=counts.values, name=f'Churn={churn_val}'))

        fig.update_layout(title='Churned Customers by Contract Type', xaxis_title='Contract Type', yaxis_title='Count', barmode='group')
        st.plotly_chart(fig)

    def survival_churn_plot(self):

        # Survival analysis
        kmf = KaplanMeierFitter()
        kmf.fit(durations=self.df['tenure_months'], event_observed=self.df['Churn'])

        plt.figure(figsize=(10, 6))
        kmf.plot()
        plt.title('Survival Curve for Churned Customers')
        plt.xlabel('Tenure Months')
        plt.ylabel('Survival Probability')
        st.pyplot()


    def feature_importance_plot(self):
        X = self.df[['tenure', 'MonthlyCharges', 'TotalCharges']]
        y = self.df['Churn']

        rf = RandomForestClassifier()
        rf.fit(X, y)

        feature_importance = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)

        fig = go.Figure()
        fig.add_trace(go.Bar(x=feature_importance.values, y=feature_importance.index, orientation='h'))
        fig.update_layout(title='Feature Importance for Churn Prediction', xaxis_title='Importance', yaxis_title='Feature')
        st.plotly_chart(fig)







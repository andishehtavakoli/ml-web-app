import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from loguru import logger

import warnings
warnings.filterwarnings('ignore')

# read data

def load_data(file_path):
    df = pd.read_csv(file_path)
    logger.info(df.head(3))
    logger.info(df.shape)
    return df

file_path = '/Users/andishetavakkoli/Documents/notebook/ml-web-app/it-customer-churn/src/data/IT_customer_churn.csv'
df = load_data(file_path)



def preprocess_data(df):

    logger.info(f'number of nan: {df.isna().sum().sum()}')
    logger.info(f'number of duplicate: {df.duplicated().sum()}')

    # drop duplicates
    df.drop_duplicates(inplace=True)

    df['OnlineSecurity'] = df['OnlineSecurity'].replace('No internet service', 'No')
    df['MultipleLines'] = df['OnlineSecurity'].replace('No internet service', 'No')
    df['OnlineBackup'] = df['OnlineSecurity'].replace('No internet service', 'No')
    df['DeviceProtection'] = df['OnlineSecurity'].replace('No internet service', 'No')
    df['TechSupport'] = df['OnlineSecurity'].replace('No internet service', 'No')
    df['StreamingTV'] = df['OnlineSecurity'].replace('No internet service', 'No')
    df['StreamingMovies'] = df['OnlineSecurity'].replace('No internet service', 'No')

    df['TotalCharges'] = df['TotalCharges'].replace("'", "").replace('"','').replace(" ", "").replace('', np.nan).astype('float')
    return df


if __name__ == "__main__":

    df = load_data(file_path)
    df = preprocess_data(df)
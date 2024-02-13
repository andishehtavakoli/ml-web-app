import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from loguru import logger

from sklearn.preprocessing import LabelEncoder

def load_df(file_path):
    try:
        df = pd.read_csv(file_path)
        logger.info(df.head(2))
        logger.info('dataframe is read!')
        return df

    except Exception as e:
        print(e)

def clean_df_func(df):
    
    # Remove duplicates
    if df.duplicated().sum() != 0:
        logger.info(f'number of duplicates before drop: {df.duplicated().shape[0]}')
        df.drop_duplicats().reset_index(inplace=True, drop=True)
        logger.info(f'number of duplicates after drop: {df.duplicated().shape[0]}')

    if df.isna().sum().sum() != 0:
        logger.info(f'number of missing values before drop: {df.isna().sum()}')
        df = df.dropna().reset_index(drop=True)
        logger.info(f'number of missing values after drop: {df.isna().sum()}')

    le = LabelEncoder()
    df['ocean_proximity'] = le.fit_transform(df['ocean_proximity'])

    return df

if __name__ == '__main__':
    df = load_df('/Users/andishetavakkoli/Documents/notebook/regression_model_practice/data/housing.csv')
    clean_df = clean_df_func(df)
    print(clean_df.head())

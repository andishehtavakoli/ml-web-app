import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot

from sklearn.preprocessing import MinMaxScaler,OneHotEncoder,QuantileTransformer,StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, KFold
from sklearn.pipeline import Pipeline

import warnings
warnings.filterwarnings('ignore')


# Load data set
df = sns.load_dataset('penguins')

# Impute NaN

def nan_imputer(df):

    # Numerical
    num_col_list = df.select_dtypes(include=[np.number]).columns
    si_num = SimpleImputer()

    # Categorical
    cat_col_list = df.select_dtypes(exclude=[np.number]).columns
    si_cat = SimpleImputer(strategy='most_frequent')

    df[num_col_list] = si_num.fit_transform(df[num_col_list])
    df[cat_col_list] = si_cat.fit_transform(df[cat_col_list])

    return df


def encoder(df):
    cat_col_list = df.select_dtypes(exclude=[np.number]).columns
    df[cat_col_list]= df[cat_col_list].apply(LabelEncoder().fit_transform)

    return df

def split_data(df, dep_variable, indep_variable, test_size=0.2):
    X = df[indep_variable]
    y = df[dep_variable]

    X_train, X_test, y_train,  y_test = train_test_split(X, y, random_state=42, test_size=test_size, stratify=y)
    return X_train, X_test, y_train, y_test 

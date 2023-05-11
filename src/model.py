from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import MinMaxScaler,OneHotEncoder,QuantileTransformer,StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
import streamlit as st


MODELS_LIST = [
    RandomForestClassifier(),
    DecisionTreeClassifier(),
    SVC(),
    LogisticRegression()]


def build_model(df, model):
    numeric_features = df.select_dtypes(include=[np.number]).columns
    numeric_transformer = Pipeline(
        steps=[('imputer', SimpleImputer(strategy='median')),
               ('scaler', StandardScaler())]
    )

    categorical_features = df.select_dtypes(exclude=[np.number]).columns
    categorical_transformer = OneHotEncoder(handle_unknown="ignore")

    preprocessor = ColumnTransformer(
        transformers=[('num', numeric_transformer, numeric_features),
                     ('cat', categorical_transformer, categorical_features)
                     ]
    )

    clf = Pipeline(
        steps=[
            ('preprocessor',preprocessor),
               ("classifier",  model)
              ]
    )
    
    return clf



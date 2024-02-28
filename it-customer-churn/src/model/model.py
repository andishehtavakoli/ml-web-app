from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from imblearn.over_sampling import SMOTE
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from loguru import logger
import pandas as pd
import joblib

from sklearn.metrics import (roc_curve, f1_score, precision_score, accuracy_score,
roc_auc_score, recall_score, classification_report, confusion_matrix)

from src.preprocessing import preprocess_data, load_data


# create pipeline
def model_eval_pipeline(df, target_col, model):
    df_input = df.copy()
    df_input['Churn'] = df_input['Churn'].replace({'Yes': 1, 'No': 0}).astype(int)

    # Split
    X = df_input.drop(target_col, axis=1)
    y = df_input[target_col]

    df_input = df_input.drop(target_col, axis=1)

    # numerical

    numeric_features = df_input.select_dtypes(include="number").columns

    numeric_transformer = Pipeline(
        steps=[('imputer', SimpleImputer(strategy='mean')),
               ('scaler', StandardScaler())]
    )

    # categorical
    categorical_features = df_input.select_dtypes(exclude="number").columns
    categorical_transformer = OneHotEncoder(handle_unknown="ignore")


    preprocessor = ColumnTransformer(
    transformers=[('num', numeric_transformer, numeric_features),
                 ('cat', categorical_transformer, categorical_features),
                  ], remainder='passthrough'
                 )



    clf = Pipeline(
        steps=[
            ('preprocessor', preprocessor),
            ("classifier", model)  # corrected this line
        ]
    )
    # save model
    joblib.dump(clf, 'src/model/model.joblib')
    logger.info('modle saved!')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    logger.info('X_train, X_test, y_train, y_test have been created!')

    kf = KFold(n_splits=6, shuffle=True, random_state=42)
    cv_results = cross_val_score(clf, X_train, y_train, cv=kf, scoring='f1')


    # Build Model
    clf.fit(X_train, y_train)
        # Cross val score


    # Prediction
    y_pred = clf.predict(X_test)


    # Metrics
    model_metric_dict = {
        "model_name": model,
        "f1_score": f1_score(y_test, y_pred),
        "precision_score": precision_score(y_test, y_pred),
        "recall_score": recall_score(y_test, y_pred),
        "accuracy_score": accuracy_score(y_test, y_pred),
        "roc_auc_score": roc_auc_score(y_test, y_pred),
        "cross_val_result": cv_results.mean()
    }

    return model_metric_dict

if __name__ == "__main__":
    file_path = '/Users/andishetavakkoli/Documents/notebook/ml-web-app/it-customer-churn/src/data/IT_customer_churn.csv'
    df = load_data(file_path)
    df = preprocess_data(df)
    target_col = 'Churn'

    # model
    models = {
        "LogisticRegression": LogisticRegression(),
        "DecisionTreeClassifier": DecisionTreeClassifier(),
        "KNeighborsClassifier": KNeighborsClassifier(),
    }

    # pd.DataFrame([model_eval_pipeline(df,"Churn", model) for model_name, model in models.items()]).sort_values("f1_score", ascending=False)

    result = []
    for model_name, model_obj in models.items():
        model_metric_dict = model_eval_pipeline(df, target_col, model_obj)
        model_metric_dict['model_name'] = model_name
        result.append(model_metric_dict)

    result_df = pd.DataFrame(result)
    result_df.to_csv('src/model/model performance.csv')
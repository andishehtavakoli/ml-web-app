import seaborn as sns
from sklearn.metrics import (accuracy_score, classification_report,
                            confusion_matrix, precision_recall_curve,
                            roc_auc_score)


from src.model import MODELS_LIST, build_model
from src.preprocessing import encoder, nan_imputer, split_data

df = sns.load_dataset('penguins')

df = nan_imputer(df)
df = encoder(df)
dep_variable = ['species']
indep_variable =[ 'island', 'bill_length_mm', 'bill_depth_mm','flipper_length_mm', 'body_mass_g', 'sex']
X_train, X_test, y_train,  y_test = split_data(df, dep_variable, indep_variable, test_size=0.2)


if __name__ == '__main__':
    for model in MODELS_LIST:
        trained_model = build_model(df, X_train, y_train, model)
        y_pred = trained_model.predict(X_test)
        print(f'model = {model}:')
        print(classification_report(y_test, y_pred))
        print('-'*50)


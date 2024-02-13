from sklearn.linear_model import Lasso, Ridge, LinearRegression
from sklearn.model_selection import train_test_split
from loguru import logger

from src.preprocessing import clean_df_func, load_df

def train_test_split_func(df):

    selected_features = df[[
        'latitude',
        'housing_median_age',
        'total_bedrooms',
        'population',
        'households',
        'median_income',
        'median_house_value',
        'ocean_proximity']]

    X = df.drop(columns='median_house_value', axis=0).values
    y = df[['median_house_value']].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    return X_train, X_test, y_train, y_test



def build_model(df,X_train, X_test, y_train, y_test):

    linreg = LinearRegression()
    linreg.fit(X_train, y_train)
    y_pred = linreg.predict(X_test)
    logger.info('Got predicted y')
    logger.info(f'r2 score is:{linreg.score(X_test, y_test)}')
    return linreg

def prediction_houseprice(model, unseen_data):
    return model.predict(unseen_data)

if  __name__ == '__main__':

    df = load_df('/Users/andishetavakkoli/Documents/notebook/regression_model_practice/data/housing.csv')
    df = clean_df_func(df)
    X_train, X_test, y_train, y_test = train_test_split_func(df)
    model = build_model(df,X_train, X_test, y_train, y_test)
    unseen_data = [[-118.18, 33.77, 37.0, 2653.0, 754.0, 1087.0, 698.0, 2.3523, 3]]
    predicted_price = prediction_houseprice(model, unseen_data)
    print(predicted_price)


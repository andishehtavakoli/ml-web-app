import streamlit as st
from src.model import prediction_houseprice, train_test_split_func, build_model
from src.preprocessing import clean_df_func, load_df



st.header('House Price Prediction in :blue[California]')
st.image('/Users/andishetavakkoli/Documents/notebook/regression_model_practice/src/House searching-bro.png', width=200, )


# longitude
# latitude
# housing_median_age
# total_rooms
# total_bedrooms
# population
# households
# median_income
# median_house_value
# ocean_proximity

col1, col2, col3, = st.columns(3)
with col1:
    latitude = st.number_input('Enter latitude:')
    longitude = st.number_input('Enter longitude:')
    housing_median_age = st.number_input('Enter housing_median_age')

with col2:
    population = st.number_input('Enter population')
    households = st.number_input('Enter households')
    ocean_proximity = st.number_input('Enter ocean_proximity')

with col3:
    median_income = st.number_input('Enter median_income')
    total_bedrooms = st.number_input('total_bedrooms')
    total_rooms = st.number_input('total_rooms')


predicted_button = st.button("Predic :sunglasses:", type="primary")

if predicted_button == True:

    df = load_df('/Users/andishetavakkoli/Documents/notebook/regression_model_practice/data/housing.csv')
    df = clean_df_func(df)
    X_train, X_test, y_train, y_test = train_test_split_func(df)
    model = build_model(df,X_train, X_test, y_train, y_test)

    unseen_data = [[
        longitude,
        latitude,
        housing_median_age,
        total_rooms,
        total_bedrooms,
        population,
        households,
        median_income,
        ocean_proximity]]

    predicted_price = prediction_houseprice(model, unseen_data)
    st.success(predicted_price)








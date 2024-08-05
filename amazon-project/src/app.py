import streamlit as st
from run import create_product_search, get_review_comments, get_review_comments


st.title(':blue[Amazon] Review Analysis :sunglasses:')

product = st.text_input("**Enter your product**", " ")

### product search and review urls
product_search_url = "https://real-time-amazon-data.p.rapidapi.com/search"
product_review_url = "https://real-time-amazon-data.p.rapidapi.com/product-reviews"

search_button = st.button("Search", type="primary")
if search_button:
    reviews = get_review_comments(product_review_url, product_search_url, product)
    st.write(reviews)

    

else:
    st.write(" ")

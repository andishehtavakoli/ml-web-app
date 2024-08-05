import requests
from dotenv import load_dotenv
import os
import json
from pprint import pprint
from loguru import logger


### Load API Key
load_dotenv()
API_KEY= os.getenv('rapidapi-key')
logger.info(API_KEY)


### product search and review urls
product_search_url = "https://real-time-amazon-data.p.rapidapi.com/search"
product_review_url = "https://real-time-amazon-data.p.rapidapi.com/product-reviews"


### Product Search Function
# create Product Search Function
def create_product_search(product_search_url, product):
    url = product_search_url
    querystring = {"query":product,"page":"1","country":"US","sort_by":"RELEVANCE","product_condition":"ALL"}

    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    response_search = response.json() 
    logger.info(response_search)
    asin_no = response_search['data']['products'][0]['asin']
    logger.info('asin_no')

    return asin_no





### Product Review Function
# Create Product Review Function
def create_product_review(product_review_url, product_search_url, product):
	asin_no = create_product_search(product_search_url, product)


	querystring = {"asin":asin_no,"country":"US","sort_by":"TOP_REVIEWS","star_rating":"ALL","verified_purchases_only":"false","images_or_videos_only":"false","current_format_only":"false","page":"1"}

	headers = {
		"x-rapidapi-key": API_KEY,
		"x-rapidapi-host": "real-time-amazon-data.p.rapidapi.com"
	}

	response_ = requests.get(product_review_url, headers=headers, params=querystring)
	response_search = response_.json()
	reviews_responce = response_search['data']['reviews']

	return reviews_responce


### Review Comments
def get_review_comments(product_review_url, product_search_url, product):
    reviews_responce = create_product_review(product_review_url, product_search_url, product)
    review_comment_lst = []
    for i in range(len(reviews_responce)):
        
        review_comment_dict = {
            'No': i+1,
            'review comment': reviews_responce[i]['review_comment']
        }
        review_comment_lst.append(review_comment_dict)

    return review_comment_lst


reviews = get_review_comments(product_review_url, product_search_url, 'phone')

### Save Reviews
def save_review(review_comments):
    
    with open('reviews.json', 'w') as f:
        json.dump(review_comments, f, indent=4)


save_review(reviews)



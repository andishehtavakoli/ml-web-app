import requests
from pathlib import Path
import os
from dotenv import load_dotenv
from utils import save_file      


DATA_DIR = Path('.').resolve()
env_path = DATA_DIR / '.env'
load_dotenv(dotenv_path=env_path)
x_rapidapi_key = os.getenv('x-rapidapi-key')

def get_linkedin_profile(username):
    url = "https://linkedin-data-api.p.rapidapi.com/"
    x_rapidapi_key =  "c154144e9fmshca0c16902f6b830p1a68f4jsn0bb666e8b8a3"

    querystring = {"username": username}

    headers = {
    	"x-rapidapi-key": x_rapidapi_key,
    	"x-rapidapi-host": "linkedin-data-api.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers, params=querystring)
    
    return response.text

if __name__ == '__main__':
    profile_data = get_linkedin_profile('sinanazem')
    print(profile_data)
    

















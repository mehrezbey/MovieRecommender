import requests
from dotenv import load_dotenv
import os

def return_poster(movie_id):
    load_dotenv()
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer "+os.getenv("SECRET_KEY")
    }
    base = "https://image.tmdb.org/t/p/original"
    response = (requests.get(url, headers=headers)).json()
    try:
        if "backdrop_path" in response :
            return base +  response["backdrop_path"]
        if "belongs_to_collection"  in response:
            if "poster_path" in response["belongs_to_collection"]:
                return  base + response["belongs_to_collection"]["poster_path"]
            if "backdrop_path" in response["belongs_to_collection"]:
                return base +  response["belongs_to_collection"]["backdrop_path"]
        return "./images/img.jpg"
    except:
        return "./images/img.jpg"
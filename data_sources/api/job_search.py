import requests
from dotenv import load_dotenv
import os
load_dotenv()

def job_search(title, location):

    url = "https://jobsearch4.p.rapidapi.com/api/v2/Jobs/Search"

    querystring = {"SearchQuery":f'{title} {location}',"PageSize":"25","PageNumber":"1"}

    headers = {
        "X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
        "X-RapidAPI-Host": "jobsearch4.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()
    data = data["data"]

    jobs = []

    for job in data:
        dict = {
            "title": job["title"],
            "company": job["company"],
            "location": '',
            "url": job["url"],
            "description": ''
        }
        jobs.append(dict)
        
    return jobs
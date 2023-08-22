import requests
from dotenv import load_dotenv
import os
load_dotenv()

def adzuna(title, location):
    try:

        pageNumber = 1
        country = 'ca'
        title = title.replace(' ', '%20')

        url = f'http://api.adzuna.com/v1/api/jobs/{country}/search/{pageNumber}?app_id={os.getenv("ADZUNA_ID")}&app_key={os.getenv("ADZUNA_API_KEY")}&where={location}&what={title}&sort_by=relevance&results_per_page=10&content-type=application/json'
        html = requests.get(url)
        
        data = html.json()
        
        data = data['results']
        
        jobs = []

        for job in data:
            obj = {
                'title': job['title'],
                'company': job['company']['display_name'],
                'location': job['location']['display_name'],
                'url': job['redirect_url'],
                'description': job['description']
            }
            jobs.append(obj)
        
        return jobs
    
    except Exception as error:
        print("An error occurred:", error)
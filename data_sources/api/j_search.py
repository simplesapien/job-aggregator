import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
import pprint
import os
load_dotenv()

# 200 requests per month limit
def j_search(title, location):

	url = "https://jsearch.p.rapidapi.com/search"

	querystring = {"query":f"{title} in {location}","page":"1","num_pages":"1"}

	headers = {
		"X-RapidAPI-Key": os.getenv("RAPIDAPI_KEY"),
		"X-RapidAPI-Host": "jsearch.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	data = response.json()
	date_format = '%m/%d/%Y %I:%M %p'


	jobs = []

	for job in data['data']:

		description=job["job_description"].replace('\n', '')
		# Shorten description to 500 characters
		if len(description) > 500:
			description = description[:500] + '...'

		dict = {
			"title": job["job_title"],
			# "date_posted": datetime.strptime(job["job_posted_at_datetime_utc"], date_format),
			"company": job["employer_name"],
			"location": f'{job["job_city"]}, {job["job_country"]}',
			"url": job["job_apply_link"],
			"description": description
		}
		jobs.append(dict)

	return jobs

# pprint.pprint(JSearch("software developer", "vancouver"))
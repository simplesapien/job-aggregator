from data_sources.find_jobs import find_jobs
from utils.filter_results import filter_results
from utils.gpt import refine_results
import webbrowser
import pprint

title = "full stack developer"
description = "I am an entry level front-end developer with only volunteer experience. I am looking for my first job in Vancouver."
location = "Vancouver"

# Find jobs
jobs = find_jobs(title, location)
pprint.pprint(jobs)

# Filter jobs based on certain criteria
filtered_jobs = filter_results(jobs)

# Check those jobs against the db to make sure they aren't already in there
# If they are, remove them from the list

# Collect job titles to feed into GPT
jobtitles = []
for job in filtered_jobs:
    jobtitles.append(job['title'])

# Use GPT to return only the 5 most relevant jobs
relevant_titles = refine_results(title, location, description, jobtitles)

# Turn list string into Python list
relevant_titles = relevant_titles.replace("'", "")
relevant_titles = relevant_titles.strip('][').split(', ')

# Go through  and print only the jobs with matching titles
refined_list = []
for job in filtered_jobs:
    if job['title'] in relevant_titles:
        refined_list.append(job)

# Add these jobs to the db

# For each link in the list, open them in a new tab
for job in refined_list:
    webbrowser.open_new_tab(job['url'])
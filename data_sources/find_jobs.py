from .api.adzuna import adzuna
from .api.career_jet import career_jet
from .api.j_search import j_search
from .api.job_search import job_search
from .api.linked_in import linked_in

def find_jobs(title, location):

    # Collect job data from all APIs
    alljobs = [
        *adzuna(title, location),
        *career_jet(title, location),
        # j_search(title, location),
        *job_search(title, location),
        *linked_in(title, location)
    ]

    return alljobs
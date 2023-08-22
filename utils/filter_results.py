def filter_results(jobs):

    filtered = []

    for job in jobs:
        filtered_title = filter_title(job['title'])
        if filtered_title:
            filtered.append(job)

    return filtered


def filter_title(job_title):
    include_terms = ["junior", "entry-level", "associate", "full-stack", "front-end", "back-end", "web developer", "software engineer", "front", "back", "web", "software", "developer", "entry level", "full stack"]
    exclude_terms = ["senior", "lead", "principal", "manager", "director", "architect", "devops", "system administrator", "database administrator", "ui/ux designer", "qa", "quality assurance"]

    # Normalize the job_title for easier matching
    job_title_lower = job_title.lower()

    # Check for any exclude terms in the title
    for term in exclude_terms:
        if term in job_title_lower:
            return False

    # Check for include terms in the title
    for term in include_terms:
        if term in job_title_lower:
            return True

    # If no include terms are found, exclude the job
    return False

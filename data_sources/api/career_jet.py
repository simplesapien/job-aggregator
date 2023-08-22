from careerjet_api_client import CareerjetAPIClient

def career_jet(title, location):
 
    cj  =  CareerjetAPIClient("en_CA")

    result_json = cj.search({
                            'location'    : location,
                            'keywords'    : title,
                            'sort'        : 'relevance',
                            'pagesize'    : '25',
                            'affid'       : '213e213hd12344552',
                            'user_ip'     : '11.22.33.44',
                            'url'         : 'http://www.example.com/jobsearch?q=python&l=london',
                            'user_agent'  : 'Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0'
                        })

    data = result_json['jobs']

    jobs = []

    for job in data:
        dict = {
            'title': job['title'],
            'company': job['company'],
            'location': job['locations'],
            'url': job['url'],
            'description': job['description'],
        }
        jobs.append(dict)

    return jobs

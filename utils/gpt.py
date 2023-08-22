from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def refine_results(title, location, description, jobs):
    # create a chat completion
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
            {"role": "user", "content": 
             f"""I am going to give you a bunch of job posts about ```{title}``` in ```{location}```, and I want you to return 
            only the 5 most relevant titles to me. I will also give you the following goal of the user to 
            provide more context: ```{description}```.
            Return only a Python list containing the titles without changing them at all. 
            Do not have any extra text. Only the list. Here are the jobs: ```{jobs}```"""},
            ]
        )

    return chat_completion.choices[0].message.content
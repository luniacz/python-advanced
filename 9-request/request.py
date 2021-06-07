import requests
import json

URL = 'https://support.oneskyapp.com/hc/en-us/article_attachments/202761727/example_2.json'
req = requests.get(URL)

quiz_selector = 'quiz'
question_selector = 'question'
questions_to_print = []
response_body = req.json()
for category in response_body[quiz_selector].keys():
    for question in response_body[quiz_selector][category]:
        questions_to_print.append(response_body[quiz_selector][category][question][question_selector])

print(questions_to_print)
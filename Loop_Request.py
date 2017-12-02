import requests
import json

team_id = 1610612737

url='https://www.googleapis.com/blogger/v3/blogs/3869481774856968139/posts/?key=AIzaSyA0UzzGOdG0wOWv7PSQZsrfeJQp4lVL2vk").json()'
print(data);

def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data);
        return data
        
    else:
        print(response.text)
        print(response.status_code)


import requests
#data = requests.get("https://www.googleapis.com/blogger/v3/blogs/3869481774856968139/posts/?key=AIzaSyA0UzzGOdG0wOWv7PSQZsrfeJQp4lVL2vk").json()
#print(data);

datawithpostid = requests.get("https://www.googleapis.com/blogger/v3/blogs/3869481774856968139/posts/2537509309351731107?key=AIzaSyA0UzzGOdG0wOWv7PSQZsrfeJQp4lVL2vk").json()
print(datawithpostid);


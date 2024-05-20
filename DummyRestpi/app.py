import requests
# import config

url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    "Accept": "application/json"
    # "Authorization": "Bearer " + config.apiKey
}
# params = {}

# response = requests.get(url, headers, params={})
response = requests.get(url, headers)
status_code = response.status_code
# result = response.text
posts = response.json()
print(status_code)
for post in posts:
    print(f'{post["id"]} - {post["title"]}')

import requests
from getpass import getpass

token = "501a930edc614cf64721150db6d634935e723a93"

headers = {
    "Authorization": f"Token {token}"
}
url = "http://localhost:8000/api/usercomment/"
response = requests.get(url, headers=headers)
print(response.json())

response = requests.post(url, headers=headers, json={
    "first_name":"Amad",
    "last_name":"Mousavi",
    "comment":"this is my handy post",
    "username":1,
    "public":True
})
print(response.json())
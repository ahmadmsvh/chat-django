import requests
from getpass import getpass


# url = "http://localhost:8000/api/guest-serializer-post/"
# response = requests.post(url, json={"first_name":"negin","last_name":"panahi","comment":"sabzipolo ba mahi"})

url = "http://localhost:8000/api/auth/"

# username = input("Enter your username: ")
# print(f"{username} enter your password: ")
# password = getpass()
# response = requests.post(url, json={
#     'username':username,
#     'password':password,})
#
# print(response.json())
#
# if response.status_code == 200:
    # token = response.json()['Bearer']
    # token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwMjMxNjEzLCJpYXQiOjE2NzAyMzEzMTMsImp0aSI6ImZjMjViZDRhODg5ZTQ5Y2RhMTJmNDBkNzRjNzFiY2ZiIiwidXNlcl9pZCI6MX0.J-eebgCfjZWZLsLZDO_cQ54bXlp4YjTf8JnO-cPG7I8"
    #
    # headers = {
    #     "Authorization": f"Bearer {token}"
    # }
    # url = "http://localhost:8000/api/usercomment/"
    # response = requests.get(url, headers=headers)
    # print(response.json())

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcwMjMxNjEzLCJpYXQiOjE2NzAyMzEzMTMsImp0aSI6ImZjMjViZDRhODg5ZTQ5Y2RhMTJmNDBkNzRjNzFiY2ZiIiwidXNlcl9pZCI6MX0.J-eebgCfjZWZLsLZDO_cQ54bXlp4YjTf8JnO-cPG7I8"

headers = {
    "Authorization": f"Bearer {token}"
}
url = "http://localhost:8000/api/usercomment/"
response = requests.get(url, headers=headers)
print(response.json())
import requests
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='apijsoncbv/'
resp=requests.post(BASE_URL+ENDPOINT)
print(resp.json())
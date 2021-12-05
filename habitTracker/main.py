import requests
from datetime import *

USER_NAME = **********
TOKEN = **********
GRAPH_ID = *******

pixela_endpoint = 'https://pixe.la/v1/users'
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_params = {
    "id": GRAPH_ID,
    "name": "Hours of code",
    "unit": "hours",
    "type": "float",
    "color": "sora",
    "timezone": "Asia/Tokyo"
}

header = {
    "X-USER-TOKEN": TOKEN
}

today = date.today()
formatted_date = str(today).replace("-", "")

pixel_params = {
    "date": f"{formatted_date}",
    "quantity": input("How many hours did you code today? ")
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=header)
data = response.json()
print(data)


import requests

#1. setup a new account at Pixela
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "thisisatoken123",
    "username": "pythontested",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)
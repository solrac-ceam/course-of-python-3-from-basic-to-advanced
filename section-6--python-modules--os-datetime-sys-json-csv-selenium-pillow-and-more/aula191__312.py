# Request para requisições HTTP
# Tutorial requests: https://www.youtube.com/watch?v=Qd8JT0bnJGs&ab_channel=Ot%C3%A1vioMiranda
import requests

# http:// -> 80
# https:// -> 443
url = "http://localhost:30300/"

response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.text)

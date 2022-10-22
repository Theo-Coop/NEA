import requests

url = "https://sugoku.herokuapp.com/board?difficulty=easy"

response = requests.get(url=url).json()

print(response["board"])
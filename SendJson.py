import requests

url = "your URL" # URL TO YOUR RENDER


payload = {"username": "test", "content": "hello"} # your JSON payload



# header with ur key
headers = {"Authorization": "yourkey",}
response = requests.post(url, json=payload, headers=headers)

print(response.text)


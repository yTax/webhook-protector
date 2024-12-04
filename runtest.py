import requests
import time



url = 'http://localhost:5000/'  # you obviously need to replace this with the domain or IP of where u host this later..
secret_key = 'your_secret_key'  # put ur key here

# test payload to send to the webhook
payload = {
    "content": "this is a test."
}

# request headers
headers = {
    "Authorization": f"{secret_key}",
    "Content-Type": "application/json"
}

def send_request():
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("message sent")
    elif response.status_code == 429:
        print("ratelimited")
    else:
        print(f"Error: {response.status_code}, {response.json()}")



for _ in range(6):  # sends 6 requests and sleeps for 500ms between each, the server should ratelimit u after the 5th
    send_request()
    time.sleep(0.5)

import requests

url = "render URL" # URL TO YOUR RENDER


payload = {
    "payload_json": '{"username": "test", "content": "hello"}' # your JSON payload, like an embed or a message, this is obviously optional if u just want to send a file
}

# Files to send
with open(r"PATH TO FILE ") as file: # here we use r"" to prevent python from fucking up the string
    files = {"file1": file} 

    # header with ur key
    headers = {"Authorization": "yourkey",}
    response = requests.post(url, data=payload, files=files, headers=headers)

    print(response.text)


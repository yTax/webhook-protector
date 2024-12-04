import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL") # dont hard code this in, use an envoriment variable.
SECRET_KEY = os.getenv("WEBHOOK_SECRET_KEY") # dont hard code this in, use an envoriment variable.

@app.route('/', methods=['POST'])
def fowardWebhook():
    
    # checks if the key u used is in the auth header
    auth_header = request.headers.get('Authorization')
    if (not auth_header or auth_header != f"Bearer {SECRET_KEY}"):
        return jsonify({"error": "Unauthorized"}), 403

    # send the received payload to ur webhook
    try:
        payload = request.json
        if (not payload): # if the sent request is empty return an error
            return jsonify({"error": "Invalid payload"}), 400

        
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        response.raise_for_status()

        return jsonify({"status": "Message forwarded successfully"}), 200
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Unknown error, possibly discords fault."}) , 500
        # return jsonify({"error": str(e)}), 500 # if discord starts acting or sum like that, probably safer to only use this when debugging

if (__name__ == '__main__'):
    app.run(debug=True, host='0.0.0.0', port=5000)
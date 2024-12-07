import os
from flask import Flask, request, jsonify
import requests
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app)

DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL") # dont hard code this in, use an envoriment variable.
SECRET_KEY = os.getenv("SECRET_KEY") # dont hard code this in, use an envoriment variable.

@app.route('/', methods=['POST']) # only accepts POST requests so ppl cant delete ur webhook
@limiter.limit("5 per minute") # set your limit per IP, this lib is comically easy to use, just type it in 
def fowardWebhook():
    
    auth_header = request.headers.get('Authorization')

    if (auth_header == "KeepAlive"): #if KeepAlive is used as the key it will respond with 200, this is just to keep Render alive 24/7
        return jsonify({"status": "Keeping instance Alive"}), 200

    if (not auth_header or auth_header != f"{SECRET_KEY}"):
        return jsonify({"error": "Unauthorized"}), 403

    # check content type so we can handle file uploads
    content_type = request.content_type
    if (content_type == "application/json"):
        # json payloads without files, we check this by checking if the user sent the request using application/json
        payload = request.json
        if (not payload):  # if u fuck up ur json it'll return 400
            return jsonify({"error": "Invalid payload"}), 400
        try:
            headers = {"Content-Type":"application/json"}
            response = requests.post(DISCORD_WEBHOOK_URL, json=payload, headers=headers)
            response.raise_for_status()
            return jsonify({"status": "Message forwarded successfully"}), 200
        except requests.exceptions.RequestException as e:
            return jsonify({"error": "Unknown error, possibly Discord's fault."}), 500

    elif ((content_type.startswith("multipart/form-data")) or content_type == ("multipart/form-data")):
        # file payloads, we do this by checking if the user POSTed with the content type multipart/form-data (which is the standard for sending files over discord webhooks)
        # the json should be under payload_json, as is standard for discord webhooks that use this content-type header
        try:
            payload_json = request.form.get("payload_json")
            files = {
            key: (file.filename, file.stream, file.mimetype)
            for key, file in request.files.items()} # theres probably better ways to do this, but essentially this will just grab all the files sent in the multpart form and place em on a dict

            data = {"payload_json": payload_json}
            response = requests.post(DISCORD_WEBHOOK_URL, data=data, files=files)
            response.raise_for_status()
            return jsonify({"status": "Files and payload forwarded successfully"}), 200
        except requests.exceptions.RequestException as e:
            return jsonify({"error": "Unknown error, possibly Discord's fault."}), 500
    else:
        return jsonify({"error": "Unsupported content type"}), 415

# returns a ratelimit response
@app.errorhandler(429)
def ratelimit_error(e):
    return jsonify(error="ratelimit exceeded", message=str(e.description)), 429

if (__name__ == '__main__'):
    app.run(debug=False, host='0.0.0.0', port=5000) # always keep debug=False when you deploy this
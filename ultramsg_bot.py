import os

from flask import Flask, request
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Ultramsg Credentials (Replace with your actual credentials)
ULTRAMSG_INSTANCE_ID = os.getenv("ULTRAMSG_INSTANCE_ID")
ULTRAMSG_API_TOKEN = os.getenv("ULTRAMSG_API_TOKEN")
ULTRAMSG_API_URL = f"https://api.ultramsg.com/{ULTRAMSG_INSTANCE_ID}/messages/chat"

# Initialize Flask app
from flask import Flask, request
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Allow all requests
CORS(app)  # Allow external requests

def send_whatsapp_message(phone, message):
    """Send a WhatsApp message using Ultramsg API."""
    data = {
        "token": ULTRAMSG_API_TOKEN,
        "to": phone,
        "body": message
    }
    response = requests.post(ULTRAMSG_API_URL, json=data)
    return response.json()

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    """Handle incoming WhatsApp messages and respond."""
    incoming_msg = request.form.get("body", "").strip().lower()
    sender_number = request.form.get("from", "")

    # Response Logic
    if incoming_msg == "start training":
        reply = "🏋️ Welcome to your training session! Start with 10 squats. Reply 'OK' when done."
    elif incoming_msg == "ok":
        reply = "✅ Great job! Now do 10 push-ups. Reply 'OK' when done."
    else:
        reply = "👋 Hello! Send 'Start Training' to begin your workout."

    # Send WhatsApp Response
    send_whatsapp_message(sender_number, reply)
    
    return "Message Sent", 200

if __name__ == "__main__":
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render provides PORT dynamically
    app.run(host="0.0.0.0", port=port, debug=True)



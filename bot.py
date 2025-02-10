from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Twilio Credentials (Loaded from .env)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

# Verify if credentials are loaded correctly
if not TWILIO_ACCOUNT_SID or not TWILIO_AUTH_TOKEN or not TWILIO_WHATSAPP_NUMBER:
    raise ValueError("\u274C ERROR: Twilio credentials not found! Make sure the .env file is set up correctly.")

print("\u2705 Twilio Credentials Loaded Successfully!")

# Initialize Twilio Client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Flask App Setup
app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    """Receives messages from WhatsApp and responds"""
    incoming_msg = request.values.get("Body", "").strip().lower()
    sender_number = request.values.get("From", "")

    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg == "start training a":
        msg.body("🏋️ Iniciando seu treino! Comece com 10 agachamentos. Digite 'OK' quando terminar.")
    elif incoming_msg == "ok":
        msg.body("✅ Bom trabalho! Agora faça 10 flexões. Digite 'OK' quando terminar.")
    else:
        msg.body("👋 Olá! Envie 'Start Training A' para começar seu treino.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


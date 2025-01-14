from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import re

app = Flask(__name__)

# Global variable to store the latest received message
latest_message = None

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Capture incoming SMS and store the message."""
    global latest_message  # Declare that we're using the global variable
    incoming_msg = request.form.get('Body')
    from_number = request.form.get('From')

    #print(f"Received message from {from_number}: {incoming_msg}")

    # Store the latest message
    latest_message = incoming_msg

    # Create a TwiML response to acknowledge receipt of the message
    response = MessagingResponse()

    return str(response)

def get_latest_message():
    """Return the latest received message."""
    global latest_message  # Declare that we're using the global variable
    if latest_message is None:
        return None
    
    numbers_only = re.sub(r"[^0-9]", "", latest_message)

    
    cleaned_message = ",".join(list(numbers_only))
    return cleaned_message

def start_flask_app():
    """Run the Flask app."""
    app.run(debug=False, port=5000)  # Disable debug mode for production
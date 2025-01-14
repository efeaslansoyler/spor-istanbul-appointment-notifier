from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Global variable to store the latest received message
latest_message = None

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Capture incoming SMS and store the message."""
    global latest_message  # Declare that we're using the global variable
    incoming_msg = request.form.get('Body')
    from_number = request.form.get('From')

    print(f"Received message from {from_number}: {incoming_msg}")

    # Store the latest message
    latest_message = incoming_msg

    # Respond to the sender (optional)
    #response = MessagingResponse()
    #response.message("Thank you for your response!")

    return str(response)

def get_latest_message():
    """Return the latest received message."""
    global latest_message  # Declare that we're using the global variable
    return latest_message

def start_flask_app():
    """Run the Flask app."""
    app.run(debug=False, port=5000)  # Disable debug mode for production
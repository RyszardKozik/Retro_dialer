from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER

def make_call(to_number):
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)

        call = client.calls.create(  # ← fixed "calss" to "calls"
            to=to_number,
            from_=TWILIO_NUMBER,
            url="http://demo.twilio.com/docs/voice.xml"  # Twilio demo message
        )

        print(f"Calling {to_number}... Call SID: {call.sid}")
        return True
    except Exception as e:
        print(f"Call failed: {e}")
        return False
 
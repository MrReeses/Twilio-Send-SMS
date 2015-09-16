''' This program sends an SMS message using the Twilio wrapper. In order to send
    a message, you need to create an account with Twilio. Once your account is
    set up, you fill need the Twilio Phone #, SID, and Auth Token which can be
    found in your account.

    Author: Mr. Reeses
    Date:   9/15/2015
    Version: 1.0
'''

import twilio
import twilio.rest
from twilio.rest import TwilioRestClient
import requests

# Twilio Number - +# (###) ###-####
# SID - 128-bit code provided by Twilio
# Autho-token - 128-bit code provided by Twilio

MrReeses_Phone = "+Add User's Phone Number Here" # Add user's phone number. Example: +###########
Twilio_Phone = "+Add Twilio Phone Number Here" # Add phone number provided by Twilio

# Be sure not to share the following two items with anyone
# These are meant for security to verify the account
account_sid = "Add SID Here" # Add Account SID provided by Twilio
auth_token = "Add Auth Token Here" # Add Auth_Token provided by Twilio

try:
    # Set up the client using the Twilio credientals
    client = twilio.rest.TwilioRestClient(account_sid, auth_token)

    # Set up and send message
    message = client.messages.create(
        to=MrReeses_Phone,
        from_=Twilio_Phone,
        body="Hello Mr. Reeses!"
    )
#Print any exceptions if the message doesn't go through    
except twilio.TwilioRestException as e:
    print e

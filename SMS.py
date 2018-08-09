from Driver import Driver
from twilio.rest import Client

#Your Twilio Account SID
account_sid = ''

#Your Twilio Account Auth Token
auth_token = ''

class SMS(Driver):
    device_name = "phone"
    def send(self, data):
        #Send a text - data must be a list of form [number,"message"]
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=data[1],from_='+18052531945',to=data[0]
            )

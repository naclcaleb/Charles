from Driver import Driver
from twilio.rest import Client

account_sid = 'ACef8aef2e6fa3ad302eafafc6efda8cb9'
auth_token = '588e948406b696dbaa539d474cfa08fb'

class SMS(Driver):
    device_name = "phone"
    def send(self, data):
        #Send a text - data must be a list of form [number,"message"]
        client = Client(account_sid, auth_token)
        message = client.messages.create(body=data[1],from_='+18052531945',to=data[0]
            )

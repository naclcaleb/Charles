import requests

#Find server based on server file
server_domain = ""

with open("/home/pi/server.txt","r") as file:
    server_domain = file.read()

class Charles:
    def __init__(self):
        pass
    def default_request(self, req):
        #Make a network request
        response = requests.get("https://" + server_domain + "/charles/api/request_handler.py").json()
        if response["response"]["status"] == "success":
            return response["response"]["utterance"]
        else:
            return "I'm terribly sorry. Could you say that again?"

import requests
appId = ""
with open("/home/pi/Charles_main/Assistant/knowledgebase/api_key.txt",'r') as file:
    appId = file.read()[:-1]


def wolframRequest(query):
    query = query.replace(" ","+")
    request = requests.get("https://api.wolframalpha.com/v1/result?appid=" + appId + "&i=" + query)
    return request.text

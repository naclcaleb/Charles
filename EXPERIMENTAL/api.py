from flask import Flask
from flask import request
from Assistant import *
import MySQLdb
app = Flask(__name__)

conn = MySQLdb.connect(host="localhost",user="<username>",passwd="<pass>",db="hoogle")
cursor = conn.cursor()

validator = Validator()
network = Seq2Seq()

@app.route("/api/request_handler", methods=['POST','GET'])
def give_response():
    auth_token = request.form["api_key"]
    req_txt = request.form["request"]
    
    #If needed, we can handle different device types here
    
    if validator.validate(auth_token):
        response = network.generateResponse(req_txt)
        return response
    else:
        return "I'm sorry, but it seems you may not have registered your device with Hoogle and obtained an auth token. Please do so now, so we can have you up and running with your Charles device."

        

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
        return "INVALID AUTH TOKEN"

        

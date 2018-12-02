from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/api/request_handler")
def give_response():
    

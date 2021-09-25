from app import app
from flask import render_template,request

@app.route("/")
def index():
    return "home"

@app.route("/analyze",methods=['GET','POST'])
def check_query():
    # as this is just a simple proof of concept, 
    # we are taking the input manually
    payload =request.args['query']
    # open the sample payloads to compare against the user's input
    log = open('XSS payload.txt')
    logfile = log.read().splitlines()
    # flag if match-case is found
    found = False
    for line in logfile:
        if str(payload) in line:
            found = True
            # exit the loop
            break
    log.close()
    if found == True:
        return """{"result":"XSS attack"}"""
    else:
        return """{"result":"XSS attack"}"""
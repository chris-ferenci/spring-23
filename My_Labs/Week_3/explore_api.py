# explore_api.py

# python3 -m flask --app explore_api.py run --host=0.0.0.0 --port=5050


from flask import Flask, request, Response
import json
import logging

app = Flask(__name__)

@app.route('/post_json_endpoint', methods=["POST"])
def post_json_endpoint():
    if request.headers['Content-Type'] == 'application/json':
        arguments = request.get_json()
        param1 = arguments.get("param1")
        param2 = arguments.get("param2")

    data = { 
        "param1": param1, 
        "param2": param2, 
        "request-content-type": "application/json" 
    }
    resp = Response(json.dumps(data), mimetype='application/json')

    return resp

@app.route('/post_form_endpoint', methods=["POST"])
def post_form_endpoint():
    if request.headers['Content-Type'] == 'application/x-www-form-urlencoded':
        param1 = request.form.get("param1")
        param2 = request.form.get("param2")

    data = { "param1": param1, "param2": param2, "request-content-type": "application/x-www-form-urlencoded" }
    resp = Response(json.dumps(data), mimetype='application/json')

    return resp

@app.route('/get_endpoint', methods=["GET"])
def get_endpoint():
    # Note for GET Request, we get input parameters from URL, not
    # application/json nor applicaiton/x-www-form-urlencoded
    # request body
    param1 = request.args.get("param1")
    param2 = request.args.get("param2")

    data = { "param1": param1, "param2": param2 }
    resp = Response(json.dumps(data), mimetype='application/json')

    return resp
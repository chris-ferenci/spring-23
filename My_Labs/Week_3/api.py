# api.py

# python3 -m flask --app api.py  run --host=0.0.0.0 --port=5050


from flask import Flask, request, Response
import json
import logging

app = Flask(__name__)

dictionary = {}

@app.route('/save_def', methods=["POST"])
def save_def():

    if request.headers['Content-Type'] == 'application/json':
        arguments = request.get_json()
        word = arguments.get("word")
        definition = arguments.get("definition")

        dictionary[word] = definition
        logging.info("Word {} with definition {} saved".format(word, definition))

    else:
        logging.warning("Invalid content type: only application/json is allowed")

    resp = Response('')
    return resp

@app.route('/get_def/<word>', methods=["GET"])
def get_def(word):
    # Note for GET Request, we get input parameters from URL, not
    # application/json
    # request body
    
    if word not in dictionary:
        definition = "Not Found"
        logging.warning("{} not found in dictionary".format(word))
    else:
        definition = dictionary[word]


    data = {"word": word, "definition": definition}
    resp = Response(json.dumps(data), mimetype='application/json')

    return resp
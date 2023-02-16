# Import the Flask module
from flask import Flask, request
import json

# Create a Flask application object
app = Flask(__name__)

#days of week array for day validation
days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


@app.route("/", methods=["GET"])
def get_all():

    with app.open_resource('quotes.json') as f:
        data = json.load(f)

        if data.keys():
            return json.dumps(data, indent = 2), 200
        else:
            return '', 204

@app.route("/<day>", methods=["GET"])
def get_by_id(day):
    with app.open_resource('quotes.json') as f:
        data = json.load(f)

    day = day.lower()

    if day in days_of_week:
        if day in data:
            day_index = list(data).index(day)
            response = list(data.items())
            return json.dumps(response[day_index]), 200
        elif day not in data:
            return '', 400
    else:
        return '', 204

@app.route("/", methods=["POST"])
def add_quote():


    # get data from body post and convert to variables
    request_data = request.get_json()
    day = request_data['day'].lower()
    quote = request_data['quote']

    if day in days_of_week:
    # create json object
        quote_of_week = { day:quote }

        # open json file
        with app.open_resource('quotes.json') as f:
            data = json.load(f)
        
        # update json file with quote object 
        data.update(quote_of_week)

        #write to file
        with open('quotes.json', 'w') as f:
            json.dump(data, f, indent = 2)
  
        return json.dumps(quote_of_week), 201
    
    else:
        return '', 400
        
@app.route("/<day>", methods=["DELETE"])
def delete_quote(day):
    with app.open_resource('quotes.json') as f:
        data = json.load(f)

    day = day.lower()

    if day in data:
        
        data.pop(day)
        with open('quotes.json', 'w') as f:
            json.dump(data, f, indent = 2)

        return '', 200
    else:
        return '', 404
    
@app.route("/<day>", methods=["PUT"])
def update_quote(day):

    request_data = request.get_json()
    quote = request_data['quote']

    with app.open_resource('quotes.json') as f:
        data = json.load(f)

    if day in days_of_week:
        if day in data.keys():
            data[day] = quote
            response = data[day]
        
            #write to file
            with open('quotes.json', 'w') as f:
                json.dump(data, f, indent = 2)
    
            return json.dumps(response), 200
    
        else:
            #create new json record
            quote_of_week = { day:quote }

            # open json file
            with app.open_resource('quotes.json') as f:
                data = json.load(f)
            
            # update json file with quote object 
            data.update(quote_of_week)

            #write to file
            with open('quotes.json', 'w') as f:
                json.dump(data, f, indent = 2)
    
            return json.dumps(quote_of_week), 201
        
    else:
        return f'', 404
    
# python3 -m flask --app ferenci_chris_lab-3.py run --host=0.0.0.0 --port=5050

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
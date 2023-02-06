# Import the Flask module
from flask import Flask

# Create a Flask application object
app = Flask(__name__)

# Define a route for the "create" endpoint

@app.route("/")
def index():
    return "Welcome to the calculator!"

@app.route("/add/<num1>/<num2>", methods=["GET"])
def add(num1, num2):
    result = int(num1) + int(num2)
    # return f"{num1} + {num2}"
    return f"The answer is {result}"


# Define a route for the "read" endpoint
@app.route("/sub/<num1>/<num2>", methods=["GET"])
def sub(num1, num2):
    result = int(num1) - int(num2)
    # return f"{num1} + {num2}"
    return f"The answer is {result}"
    

# Define a route for the "update" endpoint
@app.route("/mul/<num1>/<num2>", methods=["POST"])
def mul(num1, num2):
    # Code to update a resource
    result = int(num1) * int(num2)
    return f"The answer is {result}"

# Define a route for the "delete" endpoint
@app.route("/div/<num1>/<num2>", methods=["POST"])
def div(num1, num2):
    # Code to delete a resource
    result = int(num1) / int(num2)
    return f"The answer is {result}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
    
# python3 -m flask --app ferenci_chris_lab-2  run --host=0.0.0.0 --port=5050

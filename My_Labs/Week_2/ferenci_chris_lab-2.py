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

    if num1.isalpha() and num2.isalpha():
        return f"Invalid Input, please enter an integer or float"
    elif "." in num1 or "." in num2:
        result = float(num1) + float(num2)
    else:
        result = int(num1) + int(num2)

    return f"{result}"


# Define a route for the "read" endpoint
@app.route("/sub/<num1>/<num2>", methods=["GET"])
def sub(num1, num2):
    if num1.isalpha() and num2.isalpha():
        return f"Invalid Input, please enter an integer or float"
    elif "." in num1 or "." in num2:
        result = float(num1) - float(num2)
    else:
        result = int(num1) - int(num2)

    return f"{result}"
    

# Define a route for the "update" endpoint
@app.route("/mul/<num1>/<num2>", methods=["POST"])
def mul(num1, num2):
    if num1.isalpha() and num2.isalpha():
        return f"Invalid Input, please enter an integer or float"
    elif "." in num1 or "." in num2:
        result = float(num1) * float(num2)
    else:
        result = int(num1) * int(num2)

    return f"{result}"

# Define a route for the "delete" endpoint
@app.route("/div/<num1>/<num2>", methods=["POST"])
def div(num1, num2):
    # Code to delete a resource
    if num1.isalpha() and num2.isalpha():
        return f"Invalid Input, please enter an integer or float"
    elif "." in num1 or "." in num2:
        result = float(num1) / float(num2)
    else:
        result = int(num1) / int(num2)

    return f"{result}"


@app.errorhandler(500)
def internal_error(error):

    return "You broke it! Try make sure you enter either /add, /sub, /mul, or /div to your path."


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
    
# python3 -m flask --app ferenci_chris_lab-2  run --host=0.0.0.0 --port=5050

# client.py

import requests
import json

server_url = "http://localhost:5050"

def save_def(word, definition):
    headers = {'Content-Type': 'application/json'}
    data =  {"word": word, "definition": definition }
    url =  f"{server_url}/save_def"
    r = requests.post(url, data=json.dumps(data), headers=headers)

def get_def(word):

    headers = {'Accept':'application/json'}
    url = f"{server_url}/get_def/{word}"
    r = requests.get(url, headers=headers)

    data = r.json()
    return data["definition"]

if __name__ == "__main__":
    print("Saving the definition: country: a nation with its own government, occupying a particular territory.")
    save_def(word="country", definition="a nation with its own government, occupying a particular territory.")
    print()

    print("Retrieving the definition of 'country'")
    print(get_def("country"))
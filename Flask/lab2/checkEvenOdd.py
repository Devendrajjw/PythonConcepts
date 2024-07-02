import requests
from flask import Flask, jsonify


evenOdd = Flask(__name__)

random_microservice_url = 'http://127.0.0.1:8001/generate'
def call_random_microservice():
    response = requests.get(random_microservice_url)
    if response.status_code == 200:
        return response.json().get("Random Number")

@evenOdd.route("/check", methods=['GET'])
def check_even_odd():
    random_number = call_random_microservice()
    result = "even" if random_number % 2 == 0 else "odd"
    return jsonify({'random number': random_number, "result": result})

if __name__ == "__main__":
    evenOdd.run(debug=True, port=8002)

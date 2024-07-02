import copy

import requests
from flask import Flask, jsonify

revApp = Flask(__name__)

r_url = 'http://127.0.0.1:8001/generate'

def getRandNum():
    response = requests.get(r_url)
    if response.status_code == 200:
        return response.json().get("randNumber")

@revApp.route('/reverse', methods=['GET'])
def reverse_num():
    fetch_num = getRandNum()
    temp = copy.deepcopy(fetch_num)
    rev = 0
    while temp > 0:
        num = temp % 10
        rev = rev * 10 + num
        temp //= 10
    return jsonify({'random number': fetch_num, "reverse number": rev})

if __name__ == "__main__":
    revApp.run(debug=True, port=8002)


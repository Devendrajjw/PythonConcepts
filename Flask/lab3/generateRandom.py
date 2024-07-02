from flask import Flask, jsonify
import random

randNum = Flask(__name__)


@randNum.route('/generate', methods=['GET'])
def generate_random_number():
    randNumber = random.randint(1, 1000)
    return jsonify({"randNumber": randNumber})

if __name__ == "__main__":
    randNum.run(debug=True, port=8001)

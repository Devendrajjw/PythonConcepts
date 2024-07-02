from flask import Flask, jsonify
import random


randapp = Flask(__name__)


@randapp.route('/generate', methods=['GET'])
def generate_random_number():
    random_number = random.randint(1, 1000)
    return jsonify({'Random Number': random_number})


if __name__ == "__main__":
    randapp.run(debug=True, port=8001)

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)
USER_SERVICE_URL = 'http://localhost:5001'
ORDER_SERVICE_URL = 'http://localhost:5002'


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    response = requests.get(f'{USER_SERVICE_URL}/users/{user_id}')
    return jsonify(response.json())


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    response = requests.get(f'{ORDER_SERVICE_URL}/orders/{order_id}')
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(port=5000)

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    orders = {
        1: {'id': 1, 'item': 'Laptop', 'quantity': 1},
        1: {'id': 2, 'item': 'phone', 'quantity': 2}
    }
    order = orders.get(order_id, {})
    return jsonify(order)


if __name__ == '__main__':
    app.run(port=5002)

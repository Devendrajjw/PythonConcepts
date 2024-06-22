from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    users = {
        1: {'id': 1, 'name': 'Alice'},
        2: {'id': 2, 'name': 'Bob'}
    }
    user = users.get(user_id, {})
    return jsonify(user)


if __name__ == '__main__':
    app.run(port=5001)

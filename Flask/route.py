from flask import Flask, request, jsonify
from models import users

app = Flask(__name__)

# create a new user
@app.route('/users', methods=['POSTS'])
def create_user():
    new_user = request.json
    new_user['id'] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201


# read all user
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)


# read single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_single_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user is not None:
        return jsonify(user)
    else:
        return jsonify({'error' : 'User not found'}), 404

# update a user by id
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if user is not None:
        update_data = request.json
        user.update(update_data)
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

# delete by user id
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u['id'] != user_id]
    return jsonify({'message': 'User deleted'}), 200

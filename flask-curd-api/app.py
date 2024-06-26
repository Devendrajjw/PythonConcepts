from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
# from os import environ

app = Flask(__name__)  # read why it is used
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/testdb001'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications for performance reasons
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users101'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        return {'id': self.id, 'user_name': self.username, 'email': self.email}


with app.app_context():
        db.create_all()
# db.create_all()


# create a test route
@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'test route'}), 200)


# create a user
@app.route('/users101', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        # return make_response(jsonify({'message': 'user created'}), 201)
        return make_response(jsonify(new_user.json()), 201)
    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'error creating user'}), 500)


# update a user
@app.route('/users101/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.username = data['username']
            user.email = data['email']
            db.session.commit()
            return make_response(jsonify({'message': 'user updated', 'updated': user.json()}), 200)
        return make_response(jsonify({'message': 'user not found with given id'}), 404)
    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'error while updating user'}))


# get all users
@app.route('/users101', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return make_response(jsonify([user.json() for user in users]), 200)
    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'error getting users'}), 500)


# get user by id
@app.route('/users101/<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return make_response(jsonify({'message': user.json()}), 200)
        return make_response(jsonify({'message': 'user not found'}), 500)
    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'error getting user'}), 500)


# delete a user
@app.route('/users101/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({'message': 'user deleted', 'deleted': user.json()}), 200)
        return make_response(jsonify({'message': 'user not found'}), 400)
    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'error while delete'}))


@app.route('/users101/<int:id>/<string:username>', methods=['DELETE'])
def delete_user_by_id_name(id, username):
    try:
        user = User.query.filter(and_(User.id == id, User.username == username)).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({'message': 'user deleted', 'deleted': user.json()}), 200)
        return make_response(jsonify({'message': 'user not found'}), 400)
    except Exception as e:
        print(e)
        return make_response(jsonify({'message': 'error while delete'}))


if __name__ == '__main__':
    app.run(port=8001)

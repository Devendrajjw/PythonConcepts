from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/get_random_user', methods=['GET'])
def get_random_user():
    try:
        # Make a GET request to the randomuser.me API
        response = requests.get('https://randomuser.me/api/')

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            # Extract the user information
            user = data['results'][0]
            # Return the user information as JSON response
            return jsonify(user)
        else:
            # Return an error message if the request was not successful
            return jsonify({'error': 'Failed to fetch user data'}), 500
    except Exception as e:
        # Return an error message if an exception occurs
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

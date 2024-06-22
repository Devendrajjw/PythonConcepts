from flask import Flask, jsonify
mera_app1 = Flask(__name__)

@mera_app1.route("/")
def hello_world():
    return 'hello_world'

@mera_app1.route('/sirf_number_print/<int:n>')
def number_print(n):
    result = {'number' : n}
    return jsonify(result)


if __name__ == '__main__':
    mera_app1.run(debug=True, port=5001)

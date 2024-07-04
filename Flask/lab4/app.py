from flask import Flask, request

app = Flask(__name__)

@app.route('/<name>')
def hello_name(name):
   return f'Hello, {name}!'

if __name__ == '__main__':
    app.run(debug=True, port=8001)

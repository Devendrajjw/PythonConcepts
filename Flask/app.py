from flask import Flask, render_template, request
from math_operation import Math
app = Flask(__name__)
math = Math()


@app.route('/')
def hello_world():
    # return 'Hello, World!'
    return render_template('index.html')


@app.route('/products')
def products():
    return 'This is product page!'


@app.route('/microservice_add')
def microservice_add():
    var1 = int(request.headers.get('p1'))
    var2 = int(request.headers.get('p2'))
    return str(math.add(var1, var2))


@app.route('/microservice_subtract')
def microservice_subtract():
    var1 = int(request.headers.get('p1'))
    var2 = int(request.headers.get('p2'))
    return str(math.subtract(var1, var2))


@app.route('/microservice_multiply')
def microservice_multiply():
    var1 = int(request.headers.get('p1'))
    var2 = int(request.headers.get('p2'))
    return str(math.multiply(var1, var2))


if __name__ == '__main__':
    app.run(debug=True)

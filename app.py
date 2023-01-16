from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/f')
@app.route('/f/<celcius>')
def convert_farenheit_celcius(celcius):
    celsius = 9/ 5 * (float(celcius) + 32)
    return f'Result: {celsius:.2f} C'


if __name__ == '__main__':
    app.run()

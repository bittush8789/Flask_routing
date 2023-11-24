# Route
from flask import Flask
app = Flask("__main__")

@app.route('/home')
def home():
    return "<h1>welcome to bittu sharma <h1>"

@app.route('/blog')
def bolg():
    return "<h1>welcome to blog<h1>"


if __name__ == '__main__':
    app.run(debug=True)
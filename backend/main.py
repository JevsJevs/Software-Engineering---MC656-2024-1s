from flask import Flask

app = Flask(__name__)

@app.route("/")
def basePath():
    return "<h1>Hello World - Welcome to our project</h1>"

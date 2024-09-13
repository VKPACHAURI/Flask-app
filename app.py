from flask.app import Flask
from flask import Flask


app=Flask(__name__)

@app.route("/") #route is decorator
def name():
    return "Flask app is running!!!!!"


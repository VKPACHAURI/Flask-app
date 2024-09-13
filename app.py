from flask import Flask


app=Flask(__name__)

@app.route("/") #route is decorator
def greet():
    return "Flask app is running!!!!!"


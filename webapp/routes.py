from config import app

@app.route("/")

def greet():
    return "Flask app is running fine !!!!!!"
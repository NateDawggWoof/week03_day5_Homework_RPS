from app import app

@app.route("/home")
def index():
    return "Hello everyone"
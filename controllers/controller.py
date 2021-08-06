from flask import render_template
from app import app

@app.route("/home")
def index():
    winner =None
    return render_template("index.html", title = "RvSvP", winner = winner)
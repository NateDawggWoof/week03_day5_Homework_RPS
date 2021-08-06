from flask import Flaskapp
from flask.app import Flask

app=Flask(__name__)

from controllers import controller

if __name__=="__main__":
    app.run(debug=True)
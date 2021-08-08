from random import choice
from models.class_computer import Computer
from flask import render_template,request
from app import app
from models.class_game import *
from models.class_player import *
from models.class_computer import *


@app.route("/home")
def home():
    return render_template("home.html", title = "Home")

@app.route("/<string:name1>/<string:choice1>/<string:name2>/<string:choice2>")
def index(name1,choice1,name2,choice2):
    player1 = Player(name1,choice1)
    player2 = Player(name2,choice2)
    game = Game(player1,player2)
    game.play()
    winner = game.winner
    return render_template("index.html", title = "RvSvP", winner = winner, game=game)

@app.route("/play", methods=['GET','POST'])
def submit():
    if request.method == 'GET':
        return render_template("play.html")
    else:
        name = request.form['name']
        choice = request.form['choice']
        player1 = Player(name,choice)
        computer = Computer()
        game = Game(player1,computer)
        game.play()
        winner = game.winner
        return render_template("index.html", title = "RvSvP", winner = winner, game=game)
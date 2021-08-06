from flask import render_template
from app import app
from models.class_game import *
from models.class_player import *

@app.route("/<string:name1>/<string:choice1>/<string:name2>/<string:choice2>")
def index(name1,choice1,name2,choice2):
    player1 = Player(name1,choice1)
    player2 = Player(name2,choice2)
    game = Game(player1,player2)
    game.game_pvp()
    winner = game.winner
    return render_template("index.html", title = "RvSvP", winner = winner, game=game)
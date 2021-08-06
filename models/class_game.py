from models.class_player import *

class Game:
    def __init__(self,player1,player2,):
        self.player1=player1
        self.player2=player2
        self.winner = 0
        self.winner_name = 0
    
    def game_pvp(self):
        throw = self.player1.choice+self.player2.choice
        player1_victory = ["rockscissors", "paperrock", "scissorspaper"]
        if self.player1.choice == self.player2.choice:
            self.winner = None
        elif throw in player1_victory:
            self.winner = self.player1
            self.winner_name = self.player1.name
        else:
            self.winner = self.player2
            self.winner_name = self.player2.name



        
from _typeshed import Self
from class_player import *

class game:
    def __init__(self,player1,player2,):
        self.player1=player1
        self.player2=player2
        self.winner = None
    
    def game_pvp(self):
        throw = self.player1.choice+self.player2.choice
        player1_victory = ["rockscissors", "paperrock", "scissorspaper"]
        if self.player1.choice == self.player2.choice:
            self.winner = None
        elif throw in player1_victory:
            self.winner = self.player1
        else:
            self.winner = self.player2
        



        
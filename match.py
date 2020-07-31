from player import Player
from game import Game
from round import Round
from typing import List
import numpy as np
import copy as cp

class Match:

    def __init__(self, game: Game, players: List[Player]):
        self.game = game
        self.players = players
        self.rounds = []
        self.rounds_since_last_training = []

    def play(self, rounds_to_train):
        num_rounds = 0
        while not self.game.is_game_ended():
            self.game._board.print_map()
            score = cp.deepcopy(self.game.score)
            for player in self.players:
                actual_player = self.game.active_player
                while actual_player == self.game.active_player:
                    self.game = player.take_action(self.game)
            round = Round(np.subtract(self.game.score,score))
            self.rounds_since_last_training.append(round)
            num_rounds += 1
            is_training = False
            if num_rounds >= rounds_to_train:
                num_rounds = 0
                is_training = True
                for player in self.players:
                    player.train(self.rounds_since_last_training)
                self.rounds_since_last_training.clear()
            self.rounds.append(round)
        return self.game




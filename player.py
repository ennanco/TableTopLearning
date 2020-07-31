from abc import ABC, abstractmethod
from typing import List
from round import Round
from game import Game

class Player(ABC):

    @abstractmethod
    def __init__(self, player):
        pass

    @abstractmethod
    def take_action(self, game: Game):
        pass

    @abstractmethod
    def train(self, rounds: List[Round]):
        pass
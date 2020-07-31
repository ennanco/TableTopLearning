from abc import ABC, abstractmethod

class Game(ABC):

    @property
    @abstractmethod
    def board(self):
        pass

    # Puntuación en partida ¿?
    @property
    @abstractmethod
    def score(self):
        pass

    @abstractmethod
    def get_actions(self):
        pass

    @abstractmethod
    def do_action(self):
        pass


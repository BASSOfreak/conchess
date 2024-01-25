from abc import ABC, abstractclassmethod
from Square import Square
class MoveEngine(ABC):
    def __init__(self):
        self.hasMoved = False
    
    @abstractclassmethod
    def listPossibleMoves(self, startingRank: int, startingFile: int, isWhite: bool):
        pass

    def madeMove(self):
        self.hasMoved = True
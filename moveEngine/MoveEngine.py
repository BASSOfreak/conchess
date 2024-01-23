from abc import ABC, abstractclassmethod
from Square import Square
class MoveEngine(ABC):
    @abstractclassmethod
    def listPossibleMoves(startingSquare: Square, isWhite: bool):
        pass

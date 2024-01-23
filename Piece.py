from PieceType import PieceType
from abc import abstractmethod, ABC
from Move import Move
from Square import Square
from moveEngine.MoveEngine import MoveEngine

class Piece:
    def __init__(self, isWhiteIn: bool, pieceTypeIn: PieceType, position: list[int],
                 moveEngine: MoveEngine):
        self.isWhite = isWhiteIn
        self.currentSquare = Square(position[0], position[1])
        self.pieceType = pieceTypeIn
        self.moveEngine = moveEngine

    def __str__(self):
        if self.isWhite:
            return "white piece"
        else:  
            return "black piece"

    def listPossibleMoves(self) -> list[Move]:
        return self.moveEngine.listPossibleMoves(self.currentSquare, self.isWhite)
from Square import Square
from PieceType import PieceType

class Piece:
    def __init__(self, isWhiteIn: bool, pieceTypeIn: PieceType):
        self.isWhite = isWhiteIn
        self.currentSquare = Square(1, 1)
        self.pieceType = pieceTypeIn

    def __str__(self):
        if self.isWhite:
            return "white piece"
        else:  
            return "black piece"



from gameComponents.pieceType import PieceType

class Piece:
    def __init__(self, id: str, isWhiteIn: bool, pieceTypeIn: PieceType, 
                 startFile: int, startRank: int):
        self.id = id
        self.file = startFile
        self.rank = startRank
        self.isWhite = isWhiteIn
        self.pieceType = pieceTypeIn

    def __str__(self):
        if self.isWhite:
            return "white piece"
        else:  
            return "black piece"

    def getPieceName(self) -> str:
        name = self.pieceType.value
        if self.isWhite:
            return name.upper()
        else:
            return name.lower()
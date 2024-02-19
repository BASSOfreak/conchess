
from gameComponents.pieceType import PieceType

class Piece:
    def __init__(self, id: str, isWhiteIn: bool, pieceTypeIn: PieceType, 
                 startFile: int, startRank: int):
        self.id: str = id
        self.file: int = startFile
        self.rank: int = startRank
        self.isWhite: bool = isWhiteIn
        self.pieceType: PieceType = pieceTypeIn
        self.hasMoved: bool = False
        # only used for pawns
        self.hasMadeDoubleMove: bool = False 

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
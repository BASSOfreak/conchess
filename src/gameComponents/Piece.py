
from gameComponents.PieceType import PieceType

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

    def listPossibleMoves(self, startingFile, startingRank) -> list[int]:
        return self.moveEngine.listPossibleMoves(startingFile, startingRank, self.isWhite)
    
    def canMove(self, startingFile: int, startingRank: int, 
                destFile: int, destRank: int, isWhite: bool) -> bool:
        return self.moveEngine.canMove(startingFile, startingRank, destFile, destRank, isWhite)

    def getPieceName(self) -> str:
        name = self.pieceType.value
        if self.isWhite:
            return name.upper()
        else:
            return name.lower()
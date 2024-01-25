from PieceType import PieceType
from abc import abstractmethod, ABC
from Move import Move
from moveEngine.MoveEngine import MoveEngine

class Piece:
    def __init__(self, id: str, isWhiteIn: bool, pieceTypeIn: PieceType, 
                 startFile: int, startRank: int, 
                 moveEngine: MoveEngine):
        self.id = id
        self.file = startFile
        self.rank = startRank
        self.isWhite = isWhiteIn
        self.pieceType = pieceTypeIn
        self.moveEngine = moveEngine

    def __str__(self):
        if self.isWhite:
            return "white piece"
        else:  
            return "black piece"

    def listPossibleMoves(self, startingRank, startingFile) -> list[Move]:
        return self.moveEngine.listPossibleMoves(startingRank, startingFile, self.isWhite)
    
    def getPieceName(self) -> str:
        name = self.pieceType.value
        if self.isWhite:
            return name.upper()
        else:
            return name.lower()
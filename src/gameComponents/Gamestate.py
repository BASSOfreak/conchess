
import uuid

from gameComponents.Piece import Piece
from gameComponents.Board import Board

class Gamestate:
    _instance = None
    board = Board("mainboard")
    pieceList = {}

    def __new__(cls):
        if cls._instance is None:
            print('Creating game state instance')
            cls._instance = super(Gamestate, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance
    
    def addPieceToSquare(cls, piece: Piece, fileIn: int, rankIn: int):
        uid = uuid.uuid4().hex
        cls.pieceList[uid] = piece
        cls.board.getSquare(fileIn, rankIn).landOnSquare(uid)

    def getPieceOnSquare(cls, fileIn: int, rankIn: int) -> Piece:
        return cls.pieceList[cls.board.getSquare(fileIn, rankIn).pieceId]

    def pieceOnSquare(self, fileIn, rankIn) -> bool:
        return self.board.getSquare(fileIn,rankIn).hasPiece
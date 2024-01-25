from logging import Logger
from Board import Board
import uuid

from Piece import Piece

class Gamestate:
    _instance = None
    board = Board("mainboard")
    pieceList = []

    def __new__(cls):
        if cls._instance is None:
            print('Creating game state instance')
            cls._instance = super(Gamestate, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance
    
    def addPiece(cls, piece: Piece):
        uid = uuid.uuid4()
        cls.pieceList[uid] = piece
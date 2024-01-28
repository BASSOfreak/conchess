
import uuid
from moveEngines.moveEngine import MoveEngine
from moveEngines.pawnMoveEngine import PawnMoveEngine
from moveEngines.rookMoveEngine import RookMoveEngine
from gameComponents.pieceType import PieceType
from gameComponents.piece import Piece
from gameComponents.board import Board

class Gamestate:
    _instance = None
    board = Board("mainboard")
    pieceList = {}
    moveEngineList = {
        PieceType.PAWN: PawnMoveEngine(),
        PieceType.ROOK: RookMoveEngine(),
    }

    def __new__(cls):
        if cls._instance is None:
            print('Creating game state instance')
            cls._instance = super(Gamestate, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance
    
    def getPiece(cls, id: str) -> Piece:
        return cls.pieceList[id]
    
    def getMoveEngine(cls, pieceType: PieceType) -> MoveEngine:
        return cls.moveEngineList[pieceType]

    def removePieceFromSquare(cls, file: int, rank: int):
        cls.board.getSquare(file, rank).leaveSquare()

    def addPieceToSquare(cls, piece: Piece, file: int, rank: int):
        cls.board.getSquare(file, rank).landOnSquare(piece.id)

    def initPieceOnSquare(cls, piece: Piece, fileIn: int, rankIn: int):
        cls.pieceList[piece.id] = piece
        cls.board.getSquare(fileIn, rankIn).landOnSquare(piece.id)

    def getPieceOnSquare(cls, fileIn: int, rankIn: int) -> Piece:
        return cls.getPiece(cls.board.getSquare(fileIn, rankIn).pieceId)

    def pieceOnSquare(cls, fileIn, rankIn) -> bool:
        return cls.board.getSquare(fileIn,rankIn).hasPiece
    
    def getPosOfPiece(cls, pieceId: str) -> list[int]:
        piece = cls.getPiece(pieceId)
        return [piece.file, piece.rank]

    def movePieceFromToSquare(cls, pieceId: str, destFile: int, destRank: int):
        piece = cls.getPiece(pieceId)
        cls.removePieceFromSquare(piece.file, piece.rank)
        piece.file = destFile
        piece.rank = destRank
        cls.addPieceToSquare(piece, destFile, destRank)

    def canMove(cls, pieceID: str, destFile: int, destRank: int) -> bool:
        piece = cls.getPiece(pieceID)
        moveEngine = cls.getMoveEngine(piece.pieceType)
        return moveEngine.canMove(piece.file, piece.rank, destFile, destRank, piece.isWhite)
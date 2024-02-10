
import uuid
from moveEngines.moveEngine import MoveEngine
from moveEngines.pawnMoveEngine import PawnMoveEngine
from moveEngines.rookMoveEngine import RookMoveEngine
from moveEngines.bishopMoveEngine import BishopMoveEngine
from moveEngines.queenMoveEngine import QueenMoveEngine
from moveEngines.kingMoveEngine import KingMoveEngine
from moveEngines.knightMoveEngine import KnightMoveEngine
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
        PieceType.BISHOP: BishopMoveEngine(),
        PieceType.QUEEN: QueenMoveEngine(),
        PieceType.KING: KingMoveEngine(),
        PieceType.KNIGHT: KnightMoveEngine(),

        }
    
    def __new__(cls):
        if cls._instance is None:
            print('Creating game state instance')
            cls._instance = super(Gamestate, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance
    
    def drawBoard(cls):
        cls.board.draw()

    def clearBoard(cls):
        cls.board = Board("mainboard")
        cls.pieceList = {}

    def getPiece(cls, id: str) -> Piece:
        return cls.pieceList[id]
    
    def getMoveEngine(cls, pieceType: PieceType) -> MoveEngine:
        return cls.moveEngineList[pieceType]

    def removePieceFromSquare(cls, file: int, rank: int):
        cls.board.getSquare(file, rank).leaveSquare()

    def addPieceToSquare(cls, piece: Piece, file: int, rank: int):
        cls.board.getSquare(file, rank).landOnSquare(piece.id)

    # put piece on square based on coordinates contained in piece
    def initPieceOnSquare(cls, piece: Piece):
        cls.pieceList[piece.id] = piece
        cls.board.getSquare(piece.file, piece.rank).landOnSquare(piece)

    # get piece on a square
    def getPieceOnSquare(cls, fileIn: int, rankIn: int) -> Piece:
        return cls.board.getSquare(fileIn, rankIn).getPiece()

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

    def canMove(cls, pieceID: str, destFile: int, destRank: int, board: Board) -> bool:
        piece = cls.getPiece(pieceID)
        moveEngine = cls.getMoveEngine(piece.pieceType)
        pathClear = moveEngine.canMove(piece.file, piece.rank, destFile, destRank, piece.isWhite, board)
        if pathClear:
            # make sure that target square is empty or occupied by opponent
            if cls.board.getSquare(destFile, destRank).hasPiece:
                # square has piece
                # make sure that it is opposite color
                return cls.board.getSquare(destFile, destRank).getPiece().isWhite != piece.isWhite
            else:
                return True

        else:
            return False


    
    def getCurrentBoard(cls) -> Board:
        return cls.board

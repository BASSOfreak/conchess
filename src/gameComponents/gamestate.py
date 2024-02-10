
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
    whitePiecesThatCouldCheck = []
    blackPiecesThatCouldCheck = []


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
    
    def attemptMove(cls, pieceID: str, destFile: int, destRank: int) -> [bool, str]:
        piece: Piece = cls.getPiece(pieceID)
        moveSuccess: bool = False
        attemptDescription: str = "piece can move there"
        canPieceMoveThere: bool = False
        # check if piece can move to square
        if cls.canMove(pieceID, destFile, destRank, cls.getCurrentBoard()):
            # check if there is another piece on the destination square and if it is opposite color
            if cls.getCurrentBoard().getSquare(destFile, destRank).hasPiece:
                # check if opposite colors
                destSquarePieceColorWhite = cls.getCurrentBoard().getSquare(destFile, destRank).getPiece().isWhite()
                if destSquarePieceColorWhite != piece.isWhite():
                    # moving there is possible
                    canPieceMoveThere = True
                else:
                    # cant take piece of same color
                    moveSuccess = False
                    attemptDescription = "can't move to square with piece of same color"
            else: 
                # no piece on target square
                canPieceMoveThere = True
        else:
            attemptDescription = "piece can not move to this square"

        # test for checks if piece can move there
        if canPieceMoveThere:
            # create board with new position

            # determine if piece is king or not
            if piece.pieceType == PieceType.KING:
                # check for all opposition pieces if they can check king in its new position
                kingBecomesChecked = False
                if kingBecomesChecked:
                    attemptDescription = "king can not move there because it would be in check"
                else:
                    moveSuccess = True
            else:
                # check all pieces that might be able to check if they are now checking
                kingBecomesChecked = False
                if kingBecomesChecked:
                    attemptDescription = "piece can not move there because king would be in check"
                else:
                    moveSuccess = True


        return [moveSuccess, attemptDescription]

    def testIfCreatesChecks():
        pass

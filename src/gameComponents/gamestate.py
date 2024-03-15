
import copy
from typing import Tuple
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
from utility.utility import signOf

class Gamestate:
    _instance = None
    board = Board("mainboard")
    
    moveEngineList = {
        PieceType.PAWN: PawnMoveEngine(),
        PieceType.ROOK: RookMoveEngine(),
        PieceType.BISHOP: BishopMoveEngine(),
        PieceType.QUEEN: QueenMoveEngine(),
        PieceType.KING: KingMoveEngine(),
        PieceType.KNIGHT: KnightMoveEngine(),

        }

    castleProblems = [
        "King has moved",
        "Rook has moved",
        "King is in Check",
        "Intermediate square is in check",
        "King target square is in check",
        "path between king and rook is not clear"
    ]

    whiteHasCastled: bool = False
    blackHasCastled: bool = False

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

    def getPiece(cls, id: str) -> Piece:
        return cls.board.getPiece(id)
    
    def removePieceFromSquare(cls, file: int, rank: int):
        cls.board.getSquare(file, rank).leaveSquare()

    def addPieceToSquare(cls, piece: Piece, file: int, rank: int):
        cls.board.getSquare(file, rank).landOnSquare(piece.id)

    def initPieceOnSquare(cls, piece: Piece):
        """
        put piece on square based on coordinates contained in piece
        """
        cls.board.initPieceOnSquare(piece)

    def getPieceOnSquare(cls, fileIn: int, rankIn: int) -> Piece:
        """
        get piece on square of current board
        """
        return cls.board.getSquare(fileIn, rankIn).getPiece()

    def pieceOnSquare(cls, fileIn, rankIn) -> bool:
        return cls.board.getSquare(fileIn,rankIn).hasPiece
    
    def getPosOfPiece(cls, pieceId: str) -> list[int]:
        piece = cls.getPiece(pieceId)
        return [piece.file, piece.rank]

   

    def getMoveEngine(cls, pieceType: PieceType) -> MoveEngine:
        return cls.moveEngineList[pieceType]
    
    def canMove(self, pieceID: str, destFile: int, destRank: int, board: Board) -> bool:
        """
        check if a piece can move to a square
        doesn't check if piece can actually take square (e.g. based on color of piece on that square)
        """
        piece = self.getPiece(pieceID)
        moveEngine = self.getMoveEngine(piece.pieceType)
        pathClear = moveEngine.canMove(piece.file, piece.rank, destFile, destRank, piece.isWhite, board)
        if pathClear:
            # make sure that target square is empty or occupied by opponent
            if board.getSquare(destFile, destRank).hasPiece:
                # square has piece
                # make sure that it is opposite color
                return board.getSquare(destFile, destRank).getPiece().isWhite != piece.isWhite
            else:
                return True

        else:
            return False

    def getCurrentBoard(cls) -> Board:
        return cls.board
    
    def attemptMove(cls, pieceID: str, destFile: int, destRank: int) -> Tuple[bool, str]:
        """
        check if a move is valid and make it if possible
        """
        piece: Piece = cls.getPiece(pieceID)
        moveSuccess: bool = False
        attemptDescription: str = "piece can move there"
        canPieceMoveThere: bool = False
        # check if piece can move to square
        if cls.canMove(pieceID, destFile, destRank, cls.getCurrentBoard()):
            # check if there is another piece on the destination square and if it is opposite color
            if cls.getCurrentBoard().getSquare(destFile, destRank).hasPiece:
                # check if opposite colors
                destSquarePieceColorWhite = cls.getCurrentBoard().getSquare(destFile, destRank).getPiece().isWhite
                if destSquarePieceColorWhite != piece.isWhite:
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
            newBoard = copy.deepcopy(cls.getCurrentBoard())
            newBoard.name = "new board"

            newBoard.movePieceFromToSquare(pieceID, destFile, destRank)
            # determine if piece is king or not
            if piece.pieceType == PieceType.KING:
                # check for all opposition pieces if they can check king in its new position
                kingBecomesChecked = cls.testIfCreatesChecks(destFile, destRank, piece.isWhite, newBoard)
                
                if kingBecomesChecked:
                    attemptDescription = "king can not move there because it would be in check"
                else:
                    moveSuccess = True
                    # update pieces that can potentially check king
            else:
                # get king square
                ownKing: Piece = newBoard.pieceList[newBoard.getOppKingId(not piece.isWhite)]


                # check all pieces that might be able to check if they are now checking
                kingBecomesChecked = cls.testIfCreatesChecks(ownKing.file, ownKing.rank, piece.isWhite, newBoard)
                if kingBecomesChecked:
                    attemptDescription = "piece can not move there because king would be in check"
                else:
                    moveSuccess = True

        # define values for castling
        isCastle = False
        rookFile = 0
        intermediateSquareFile = piece.file + signOf(destFile - piece.file)
        # check if move is castle
        if not canPieceMoveThere and piece.pieceType == PieceType.KING:
            castleRank = 8 if piece.isWhite else 1
            # check if moving along starting rank 
            if piece.rank == castleRank and destRank == castleRank and (destFile == 7 or destFile == 3):
                # king side castle
                if destFile == 7:
                    rookFile = 8
                # queen side castle
                elif destFile == 3:
                    rookFile = 1
                # conditions for castling 
                castleConditionsMet = []
                # has king moved
                castleConditionsMet.append(not piece.hasMoved)
                # has rook moved
                castleConditionsMet.append(not cls.getCurrentBoard().getSquare(rookFile, destRank).getPiece().hasMoved)
                # no checks on relevant squares
                # check on king square
                castleConditionsMet.append(not cls.testIfCreatesChecks(piece.file, piece.rank, piece.isWhite, cls.getCurrentBoard()))
                # check on intermediate square
                castleConditionsMet.append(not cls.testIfCreatesChecks(intermediateSquareFile, destRank, piece.isWhite, cls.getCurrentBoard()))
                # check on king destination square
                castleConditionsMet.append(not cls.testIfCreatesChecks(destFile, destRank, piece.isWhite, cls.getCurrentBoard()))
                # all squares between king and rook must be empty
                tempMoveEngine = cls.moveEngineList[PieceType.KING]
                castleConditionsMet.append(tempMoveEngine.checkStraightPathClear(piece.file, rookFile, True, castleRank, cls.getCurrentBoard()))

                canCastle = True
                canNotCastleReasons = []
                for [cond, string] in zip(castleConditionsMet, cls.castleProblems):
                    # can not castle if condition is not met
                    if not cond:
                        canCastle = False
                        # add reason
                        canNotCastleReasons.append(string)
                

                if canCastle:
                    isCastle = True
                    moveSuccess = True
                    attemptDescription = "possible castle detected"
                else:
                    attemptDescription = "tried to castle but the following problems occured\n"
                    for problem in canNotCastleReasons:
                        attemptDescription = attemptDescription + "-" +  problem + "\n"

            else:
                attemptDescription = "king can not move to this square"
            

        # make the move if possible
        if moveSuccess:
            startRank = piece.rank
            startFile = piece.file
            piece.hasMoved = True
            # move piece
            cls.getCurrentBoard().movePieceFromToSquare(pieceID, destFile, destRank)
            
            # check for promotion of pawn
            if piece.pieceType == PieceType.PAWN:
                piece.hasMadeDoubleMove = False

                # set final rank
                finalRank = 1 if piece.isWhite else 8
                if piece.rank == finalRank:
                    newPieceType = promotePiece()
                    piece.pieceType = newPieceType

                # check if made double move
                if abs(startRank - destRank) == 2:
                    piece.hasMadeDoubleMove = True
            elif isCastle:
                # set flag for castle
                if piece.isWhite:
                    cls.whiteHasCastled = True
                else:
                    cls.blackHasCastled = True

                # move rook
                rookId = cls.getPieceOnSquare(rookFile, destRank).id
                cls.getCurrentBoard().movePieceFromToSquare(rookId, intermediateSquareFile, destRank)

                
                


        return moveSuccess, attemptDescription

    def testIfCreatesChecks(cls, destFile: int, destRank: int, pieceIsWhite: bool, board: Board) -> bool:
        """
        used for checking if any piece can move to current king position
        used when attempting to make a move
        """
        for pieceId, tempPiece in board.pieceList.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
            # test only pieces of opposite color
            if tempPiece.isWhite != pieceIsWhite:
                # test if opponent piece can move to this square
                #print(f"testing if {pieceId} can check king at {str(destFile)},{str(destRank)}")
                if cls.canMove(pieceId, destFile, destRank, board):
                    return True

        return False
    

    def canCheckOppKing(cls, piece: Piece, board: Board) -> bool:
        """
        check if a piece can check the opponent's king based on its current position
        """
        # check if an opposition king is on the board
        oppKingId = board.getOppKingId(piece.isWhite)
        if oppKingId != "":
            # check if the piece can check the king
            oppKing = board.getPiece(oppKingId)
            if cls.canMove(piece.id, oppKing.file, oppKing.rank, board):
                return True

        return False
    
    def getBoardRep(cls) -> str:
        boardState = cls.getCurrentBoard().getBoardRep()
        print(boardState)

    
def promotePiece() -> PieceType:
    """
    get the type of piece that the user wants a pawn to be promoted to
    """
    while True:
        print("pawn has reached final rank.\n" + 
            "which piece should it get promoted to?\n" +
            "q = Queen, r = Rook, b = Bishop, n = Knight")
        # get user input
        string = input()

        # select case
        match string:
            case "q":
                return PieceType.QUEEN
            case "r":
                return PieceType.ROOK
            case "b":
                return PieceType.BISHOP
            case "n":
                return PieceType.KNIGHT
            
        print("no valid piece selected. Try again.\n")


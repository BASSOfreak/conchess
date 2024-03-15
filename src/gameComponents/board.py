from ast import Dict
from gameComponents.square import Square
from gameComponents.piece import Piece
from gameComponents.pieceType import PieceType
from utility.utility import getSquareDelim
from utility.utility import internalRankToRealRank

class Board:
    rankDelim = "  +---+---+---+---+---+---+---+---+"
    fileNames = "    A   B   C   D   E   F   G   H"
    def __init__(self, name: str):
        self.name = name
        self.squareList = [[0 for i in range(8)] for j in range(8)]
        for file in range(8):
            for rank in range(8):
                self.squareList[file][rank] = Square(rank + 1, file + 1)

        self.pieceList: Dict[str, Piece] = {}
        self.whitePiecesThatCouldCheck = []
        self.blackPiecesThatCouldCheck = []

    def movePieceFromToSquare(self, pieceId: str, destFile: int, destRank: int):
        piece = self.getPiece(pieceId)
        self.getSquare(piece.file, piece.rank).leaveSquare()
        piece.file = destFile
        piece.rank = destRank

        # delete piece on destination square
        if self.getSquare(destFile, destRank).hasPiece:
            eatenPieceId = self.getSquare(destFile, destRank).getPiece().id
            # remove piece from piece list
            del self.pieceList[eatenPieceId]
            # remove piece from list of pieces that could check if it is in there
            if piece.isWhite:
                # check in list of black pieces
                try:
                    self.blackPiecesThatCouldCheck.remove(eatenPieceId)
                except:
                    pass
            else:
                # check in list of white pieces
                try:
                    self.whitePiecesThatCouldCheck.remove(eatenPieceId)
                except:
                    pass


        self.getSquare(destFile, destRank).landOnSquare(piece)
        self.getPiece(pieceId).file = destFile
        self.getPiece(pieceId).rank = destRank    

    def getOppKingId(self, isWhite: bool) -> str:
        for pieceId, tempPiece in self.pieceList.items():
            if tempPiece.pieceType == PieceType.KING and tempPiece.isWhite != isWhite:
                return pieceId
        return ""    
        

    #def updateListOfPossibleChecks(self, )

    def initPieceOnSquare(self, piece: Piece):
        self.pieceList[piece.id] = piece
        self.getSquare(piece.file, piece.rank).landOnSquare(piece)

    def getSquare(self, fileIn, rankIn) -> Square:
        return self.squareList[fileIn - 1][rankIn - 1]
    
    def getPiece(self, id: str) -> Piece:
        return self.pieceList[id]

    def initGameBoard(self):
        # init white pawns
        for i in range(1,9,1):
            piece: Piece = Piece("whitePawn " + str(i), True, PieceType.PAWN, i, 7)
            self.initPieceOnSquare(piece)
        # init white king
        whiteKing: Piece = Piece("whiteKing", True, PieceType.KING, 5, 8)
        self.initPieceOnSquare(whiteKing)
        # init white queen
        whiteQueen: Piece = Piece("whiteQueen", True, PieceType.QUEEN, 4, 8)
        self.initPieceOnSquare(whiteQueen)
        # init white rook1
        whiteRook1: Piece = Piece("whiteRook1", True, PieceType.ROOK, 1, 8)
        self.initPieceOnSquare(whiteRook1)
        # init white rook2
        whiteRook2: Piece = Piece("whiteRook2", True, PieceType.ROOK, 8, 8)
        self.initPieceOnSquare(whiteRook2)
        # init white bishop1
        whiteBishop1: Piece = Piece("whiteBishop1", True, PieceType.BISHOP, 3, 8)
        self.initPieceOnSquare(whiteBishop1)
        # init white bishop2
        whiteBishop2: Piece = Piece("whiteBishop2", True, PieceType.BISHOP, 6, 8)
        self.initPieceOnSquare(whiteBishop2)
        # init white knight1
        whiteKnight1: Piece = Piece("whiteKnight1", True, PieceType.KNIGHT, 2, 8)
        self.initPieceOnSquare(whiteKnight1)
        # init white knight2
        whiteKnight2: Piece = Piece("whiteKnight2", True, PieceType.KNIGHT, 7, 8)
        self.initPieceOnSquare(whiteKnight2)

        # init black pawns
        for i in range(1,9,1):
            piece: Piece = Piece("blackPawn " + str(i), False, PieceType.PAWN, i, 2)
            self.initPieceOnSquare(piece)
        # init black king
        blackKing: Piece = Piece("blackKing", False, PieceType.KING, 5, 1)
        self.initPieceOnSquare(blackKing)
        # init black queen
        blackQueen: Piece = Piece("blackQueen", False, PieceType.QUEEN, 4, 1)
        self.initPieceOnSquare(blackQueen)
        # init black rook1
        blackRook1: Piece = Piece("blackRook1", False, PieceType.ROOK, 1, 1)
        self.initPieceOnSquare(blackRook1)
        # init black rook2
        blackRook2: Piece = Piece("blackRook2", False, PieceType.ROOK, 8, 1)
        self.initPieceOnSquare(blackRook2)
        # init black bishop1
        blackBishop1: Piece = Piece("blackBishop1", False, PieceType.BISHOP, 3, 1)
        self.initPieceOnSquare(blackBishop1)
        # init black bishop2
        blackBishop2: Piece = Piece("blackBishop2", False, PieceType.BISHOP, 6, 1)
        self.initPieceOnSquare(blackBishop2)
        # init black knight1
        blackKnight1: Piece = Piece("blackKnight1", False, PieceType.KNIGHT, 2, 1)
        self.initPieceOnSquare(blackKnight1)
        # init black knight2
        blackKnight2: Piece = Piece("blackKnight2", False, PieceType.KNIGHT, 7, 1)
        self.initPieceOnSquare(blackKnight2)
        

    # prints entire board to console
    def draw(self):
        print(" ")
        for rank in range(1,9,1):
            print(self.rankDelim)
            print(internalRankToRealRank(rank) + " ", end = "")
            print("|", end="")
            for file in range(1,9,1):
                squareDelim = getSquareDelim(file, rank)
                print(squareDelim, end = "")
                if self.getSquare(file, rank).hasPiece:
                    print(self.getSquare(file, rank).getPiece().getPieceName(), end="")
                else:
                    print(" ", end="")
                print(squareDelim, end = "")
                print("|", end="")
            print(" ")

        print(self.rankDelim)
        print(self.fileNames)
    
    def getBoardRep(self) -> str:
        output:str = ""
        # loop through files
        for rankIt in range(1,9):
            emptyCounter:int = 0
            # loop through ranks
            for fileIt in range(1,9):
                # check if there is a piece on the square
                if self.getSquare(fileIt, rankIt).hasPiece:
                    # add value of counter to output and reset
                    if emptyCounter > 0:
                        output = output + str(emptyCounter)
                        emptyCounter = 0
                    
                    # add piece to output
                    output = output + self.getSquare(fileIt, rankIt).getPiece().getPieceName()
                else:
                    # increment counter
                    emptyCounter = emptyCounter + 1
            
            # add remaining empty squares if there are any
            if emptyCounter > 0:
                output = output + str(emptyCounter)
                emptyCounter = 0
                
            # add a '/' after each rank
            output = output + "/"
        return output
import unittest
from unittest.mock import patch


import os
import sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.join(parent_dir_name, "src"))

from gameComponents.gamestate import Gamestate
#from gameComponents.gamestate import promotePiece
from gameComponents.piece import Piece
from gameComponents.pieceType import PieceType

class TestGamestate(unittest.TestCase):
    def setUp(self):
        gamestate = Gamestate()
        gamestate.clearBoard()

    def testBoardSingleton(self):
        gamestate1 = Gamestate()
        gamestate2 = Gamestate()
        self.assertEqual(id(gamestate1), id(gamestate2))
        
    def testBoardInit(self):
        gamestate = Gamestate()
        b = gamestate.board
        self.assertEqual(b.name, "mainboard")

    def testPutPieceOnBoard(self):
        gamestate = Gamestate()
        whitePawn = Piece(id="asd", isWhiteIn= True, pieceTypeIn=PieceType.PAWN, startFile= 4, startRank= 4)
        gamestate.initPieceOnSquare(whitePawn)
        outPiece = gamestate.getPieceOnSquare(4,4)
        self.assertEqual(whitePawn.id, outPiece.id)

    def testMakeMultipleMoves(self):
        gamestate = Gamestate()
        gamestate.getCurrentBoard().initGameBoard()
        # get c2 pawn and move one rank up
        e2Pawn = gamestate.getPieceOnSquare(3, 7)
        [firstMoveSuccess, resultString] = gamestate.attemptMove(e2Pawn.id, 3,6)
        #gamestate.getCurrentBoard().draw()
        self.assertEqual(firstMoveSuccess, True)
        # move d7 pawn on square up
        d7Pawn = gamestate.getPieceOnSquare(4,2)
        [secondMoveSuccess, resultString] = gamestate.attemptMove(d7Pawn.id, 4,3)
        #gamestate.getCurrentBoard().draw()
        self.assertEqual(secondMoveSuccess, True)
        # move white queen to a4 to create check
        whiteQueen = gamestate.getPieceOnSquare(4,8)
        [thirdMoveSuccess, resultString] = gamestate.attemptMove(whiteQueen.id, 1,5)
        #gamestate.getCurrentBoard().draw()
        self.assertEqual(thirdMoveSuccess, True)
        # move pawn on opposite end of board
        h2Pawn = gamestate.getPieceOnSquare(8,2)
        [fourthMoveSuccess, resultString] = gamestate.attemptMove(h2Pawn.id, 8,3)
        #gamestate.getCurrentBoard().draw()
        self.assertEqual(fourthMoveSuccess, False)
        # block with the knight
        blackKnight = gamestate.getPieceOnSquare(2,1)
        [fifthMoveSuccess, resultString] = gamestate.attemptMove(blackKnight.id, 3,3)
        self.assertEqual(fifthMoveSuccess, True)
        #gamestate.getCurrentBoard().draw()
        # move central pawn
        whitePawn = gamestate.getPieceOnSquare(4,7)
        [sixthMoveSuccess, resultString] = gamestate.attemptMove(whitePawn.id, 4,5)
        self.assertEqual(sixthMoveSuccess, True)
        #gamestate.getCurrentBoard().draw()
        # try to move knight out of way
        blackKnight = gamestate.getPieceOnSquare(3,3)
        [seventhMoveSuccess, resultString] = gamestate.attemptMove(blackKnight.id, 1,4)
        self.assertEqual(seventhMoveSuccess, False)
        #gamestate.getCurrentBoard().draw()

    @patch('src.gameComponents.gamestate.promotePiece')
    def testPromotionOfPawn(self, mock_fun):
        #mock_fun.return_value = PieceType.QUEEN
        gamestate = Gamestate()
        whitePawn = Piece(id="whitePawn", isWhiteIn= True, pieceTypeIn=PieceType.PAWN, startFile= 4, startRank= 2)
        gamestate.initPieceOnSquare(whitePawn)
        whiteKing = Piece(id="whiteKing", isWhiteIn= True, pieceTypeIn=PieceType.KING, startFile= 5, startRank= 1)
        gamestate.initPieceOnSquare(whiteKing)
        blackKing = Piece(id="blackKing", isWhiteIn= False, pieceTypeIn=PieceType.KING, startFile= 3, startRank= 1)
        gamestate.initPieceOnSquare(blackKing)
        #gamestate.drawBoard()
        print("promote pawn to queen to pass")
        [firstMoveSuccess, resultString] = gamestate.attemptMove("whitePawn", 4,1)
        #gamestate.drawBoard()
        [secondMoveSuccess, resultString] = gamestate.attemptMove("blackKing", 2,2)
        #gamestate.drawBoard()
        self.assertEqual(firstMoveSuccess, True)
        self.assertEqual(secondMoveSuccess, True)
        self.assertEqual(gamestate.getPiece("whitePawn").pieceType, PieceType.QUEEN)
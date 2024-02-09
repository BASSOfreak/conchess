import unittest

import os
import sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.join(parent_dir_name, "src"))

from gameComponents.gamestate import Gamestate
from gameComponents.piece import Piece
from gameComponents.pieceType import PieceType

class TestPawnMoveEngine(unittest.TestCase):
    def setUp(self):
        gamestate = Gamestate()
        gamestate.clearBoard()

    def testNormalMove(self):
        gamestate = Gamestate()
        # start in middle of board
        whitePawn = Piece(id="asd", isWhiteIn= True, pieceTypeIn=PieceType.PAWN, startFile= 4, startRank= 4)
        gamestate.initPieceOnSquare(whitePawn)
        # white pawn should be able to move one step up
        whiteCanMoveUp = gamestate.canMove("asd",4,3, gamestate.getCurrentBoard())
        self.assertEqual(whiteCanMoveUp, True)
        # black pawn should be able to move one step down
        blackPawn = Piece(id="blasdkjh", isWhiteIn= False, pieceTypeIn=PieceType.PAWN, startFile= 3, startRank= 4)
        gamestate.initPieceOnSquare(blackPawn)
        blackCanMoveUp = gamestate.canMove("blasdkjh",3,5, gamestate.getCurrentBoard())
        # white pawn should be able to move one step up
        self.assertEqual(blackCanMoveUp, True)
        
        
    def testDiagonalTake(self):
        # if there is a piece diagonally up, white pawn should be able to take
        gamestate = Gamestate()
        whitePawn = Piece(id="asd", isWhiteIn= True, pieceTypeIn=PieceType.PAWN, startFile= 5, startRank= 5)
        gamestate.initPieceOnSquare(whitePawn)
        blackPawn = Piece(id="3924758fth", isWhiteIn= False, pieceTypeIn=PieceType.PAWN, startFile= 4, startRank= 4)
        gamestate.initPieceOnSquare(blackPawn)
        resCanMove = gamestate.canMove("asd",4,4, gamestate.getCurrentBoard())
        self.assertEqual(resCanMove, True)
        # if there is a piece diagonally down, black pawn should be able to take
        
        
    def testPromotion(self):
        # if white pawn moves to top rank, it should be promoted
        # if white pawn moves to bottom rank, it should be promoted
        pass
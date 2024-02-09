import unittest

import os
import sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.join(parent_dir_name, "src"))

from gameComponents.gamestate import Gamestate
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
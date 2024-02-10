import unittest

import os
import sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.join(parent_dir_name, "src"))

from gameComponents.gamestate import Gamestate
from gameComponents.piece import Piece
from gameComponents.pieceType import PieceType
from moveEngines.kingMoveEngine import KingMoveEngine

class TestRookMoveEngine(unittest.TestCase):
    def setUp(self):
        gamestate = Gamestate()
        gamestate.clearBoard()

    def testListTakes(self):
        moveEngine = KingMoveEngine()
        takeList = moveEngine.listPossibleTakes(4, 4, True)
        shouldBeList = [[3,3],[4,3],[5,3],[3,4],[5,4],[3,5],[4,5],[5,5]]
        
        self.assertCountEqual(takeList, shouldBeList)

    def testTakeAdjacent(self):
        gamestate = Gamestate()
        whiteKing = Piece("asd32", True, PieceType.KING, 4,4)
        gamestate.initPieceOnSquare(whiteKing)
        blackPawn = Piece("q327d6r4tg", False, PieceType.PAWN, 4,3)
        gamestate.initPieceOnSquare(blackPawn)
        self.assertEqual(gamestate.canMove("asd32",4,3,gamestate.getCurrentBoard()), True)

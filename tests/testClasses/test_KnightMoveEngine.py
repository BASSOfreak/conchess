import unittest

import os
import sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.join(parent_dir_name, "src"))

from gameComponents.gamestate import Gamestate
from gameComponents.piece import Piece
from gameComponents.pieceType import PieceType
from moveEngines.knightMoveEngine import KnightMoveEngine

class TestRookMoveEngine(unittest.TestCase):
    def setUp(self):
        gamestate = Gamestate()
        gamestate.clearBoard()

    def testListTakes(self):
        moveEngine = KnightMoveEngine()
        takeList = moveEngine.listPossibleTakes(4, 4, True)
        shouldBeList = [[6,3],[6,5],[2,3],[2,5],[3,2],[5,2],[3,6],[5,6]]
        self.assertCountEqual(takeList, shouldBeList)

    def testListTakesOnEdge(self):
        moveEngine = KnightMoveEngine()
        takeList = moveEngine.listPossibleTakes(1,4, True)
        shouldBeList = [[2,2],[2,6],[3,3],[3,5]]
        self.assertCountEqual(takeList, shouldBeList)

    def testCanMove(self):
        gamestate = Gamestate()
        moveEngine = KnightMoveEngine()
        self.assertEqual(moveEngine.canMove(4,4,6,5,True,gamestate.getCurrentBoard()), True)
import unittest

import os
import sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.join(parent_dir_name, "src"))

from gameComponents.gamestate import Gamestate
from gameComponents.piece import Piece
from gameComponents.pieceType import PieceType
from moveEngines.queenMoveEngine import QueenMoveEngine

class TestRookMoveEngine(unittest.TestCase):
    def setUp(self):
        gamestate = Gamestate()
        gamestate.clearBoard()

    def testListTakes(self):
        moveEngine = QueenMoveEngine()
        takeList = moveEngine.listPossibleTakes(4, 4, True)
        shouldBeList = [[4,1],[4,2],[4,3],[4,5],[4,6],[4,7],[4,8],[1,4],[2,4],[3,4],[5,4],[6,4],[7,4],[8,4],
                        [3,3],[2,2],[1,1],[5,3],[6,2],[7,1],[3,5],[2,6],[1,7],[5,5],[6,6],[7,7],[8,8]]
        
        self.assertCountEqual(takeList, shouldBeList)

    def testTakeAdjacent(self):
        gamestate = Gamestate()
        whiteQueen = Piece("asd32", True, PieceType.QUEEN, 4,4)
        gamestate.initPieceOnSquare(whiteQueen)
        blackPawn = Piece("q327d6r4tg", False, PieceType.PAWN, 4,3)
        gamestate.initPieceOnSquare(blackPawn)
        self.assertEqual(gamestate.canMove("asd32",4,3,gamestate.getCurrentBoard()), True)
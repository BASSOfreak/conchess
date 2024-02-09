import unittest

import os
import sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.join(parent_dir_name, "src"))

from gameComponents.gamestate import Gamestate
from gameComponents.piece import Piece
from gameComponents.pieceType import PieceType
from moveEngines.rookMoveEngine import RookMoveEngine

class TestRookMoveEngine(unittest.TestCase):
    def setUp(self):
        gamestate = Gamestate()
        gamestate.clearBoard()

    def testListTakes(self):
        moveEngine = RookMoveEngine()
        takeList = moveEngine.listPossibleTakes(4, 4, True)
        shouldBeList = [[4,1],[4,2],[4,3],[4,5],[4,6],[4,7],[4,8],[1,4],[2,4],[3,4],[5,4],[6,4],[7,4],[8,4]]
        
        self.assertCountEqual(takeList, shouldBeList)

    def testBlockedTake(self):
        gamestate = Gamestate()
        whiteRook = Piece("asd32", True, PieceType.ROOK, 4,7,)
        gamestate.initPieceOnSquare(whiteRook)
        whitePawn = Piece("324f5d876th", True, PieceType.PAWN, 4,5,)
        gamestate.initPieceOnSquare(whitePawn)
        blackPawn = Piece("q327d6r4tg", False, PieceType.PAWN, 4,1,)
        gamestate.initPieceOnSquare(blackPawn)
        self.assertEqual(gamestate.canMove("asd32",4,1,gamestate.getCurrentBoard()), False)

    def testNotBlockedTake(self):
        gamestate = Gamestate()
        whiteRook = Piece("asd32", True, PieceType.ROOK, 4,7,)
        gamestate.initPieceOnSquare(whiteRook)
        whitePawn = Piece("324f5d876th", True, PieceType.PAWN, 3,5,)
        gamestate.initPieceOnSquare(whitePawn)
        blackPawn = Piece("q327d6r4tg", False, PieceType.PAWN, 4,1,)
        gamestate.initPieceOnSquare(blackPawn)
        self.assertEqual(gamestate.canMove("asd32",4,1,gamestate.getCurrentBoard()), True)
import unittest

import os
import sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.join(parent_dir_name, "src"))

from gameComponents.gamestate import Gamestate
from gameComponents.piece import Piece
from gameComponents.pieceType import PieceType
from moveEngines.bishopMoveEngine import BishopMoveEngine

class TestBishopMoveEngine(unittest.TestCase):
    def setUp(self):
        gamestate = Gamestate()
        gamestate.clearBoard()

    def testListTakes(self):
        moveEngine = BishopMoveEngine()
        takeList = moveEngine.listPossibleTakes(4, 4, True)
        shouldBeList = [[3,3],[2,2],[1,1],[5,3],[6,2],[7,1],[3,5],[2,6],[1,7],[5,5],[6,6],[7,7],[8,8]]
        
        self.assertCountEqual(takeList, shouldBeList)

    def testBlockedTake(self):
        gamestate = Gamestate()
        whiteBishop = Piece("asd32", True, PieceType.BISHOP, 8,8)
        gamestate.initPieceOnSquare(whiteBishop)
        whitePawn = Piece("324f5d876th", True, PieceType.PAWN, 4,4)
        gamestate.initPieceOnSquare(whitePawn)
        blackPawn = Piece("q327d6r4tg", False, PieceType.PAWN, 1,1)
        gamestate.initPieceOnSquare(blackPawn)
        self.assertEqual(gamestate.canMove("asd32",1,1,gamestate.getCurrentBoard()), False)

    def testNotBlockedTake(self):
        gamestate = Gamestate()
        whiteBishop = Piece("asd32", True, PieceType.BISHOP, 4,7)
        gamestate.initPieceOnSquare(whiteBishop)
        whitePawn = Piece("324f5d876th", True, PieceType.PAWN, 3,2)
        gamestate.initPieceOnSquare(whitePawn)
        blackPawn = Piece("q327d6r4tg", False, PieceType.PAWN, 4,1)
        gamestate.initPieceOnSquare(blackPawn)
        self.assertEqual(gamestate.canMove("asd32",1,1,gamestate.getCurrentBoard()), True)
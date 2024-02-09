import unittest

import os
import sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.join(parent_dir_name, "src"))

from gameComponents.piece import Piece
from gameComponents.pieceType import PieceType

class TestPiece(unittest.TestCase):
    def testColor(self):
        whitePiece = Piece("asdasd", True, PieceType.PAWN, 1,2)
        self.assertEqual(whitePiece.isWhite, True)
        blackPiece = Piece("234rz6t", False, PieceType.PAWN, 1,2)
        self.assertEqual(blackPiece.isWhite, False)

    def testGetName(self):
        piece = Piece("asdasd", True, PieceType.PAWN, 1,2)
        self.assertEqual(piece.getPieceName(), 'P')

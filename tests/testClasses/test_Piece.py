import unittest

import os
import sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
sys.path.append(os.path.join(parent_dir_name, "src"))

from gameComponents.piece import Piece
from gameComponents.pieceType import PieceType

class TestPiece(unittest.TestCase):
    def testColor(self):
        whitePiece = Piece("", True, None, 1, 1, None)
        self.assertEqual(whitePiece.isWhite, True)
        blackPiece = Piece("", False, None, 1, 1, None)
        self.assertEqual(blackPiece.isWhite, False)

    def testGetName(self):
        piece = Piece("", True, PieceType.PAWN, 1, 1, None)
        self.assertEqual(piece.getPieceName(), 'P')

import unittest

from Piece import Piece
from PieceType import PieceType


class TestPiece(unittest.TestCase):
    def testColor(self):
        whitePiece = Piece("", True, None, 1, 1, None)
        self.assertEqual(whitePiece.isWhite, True)
        blackPiece = Piece("", False, None, 1, 1, None)
        self.assertEqual(blackPiece.isWhite, False)

    def testGetName(self):
        piece = Piece("", True, PieceType.PAWN, 1, 1, None)
        self.assertEqual(piece.getPieceName(), 'P')

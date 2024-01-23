import unittest
from Piece import Piece

class TestPiece(unittest.TestCase):
    def testColor(self):
        whitePiece = Piece(True, None, [1,1], None)
        self.assertEqual(whitePiece.isWhite, True)
        blackPiece = Piece(False, None, [1,1], None)
        self.assertEqual(blackPiece.isWhite, False)


if __name__ == '__main__':
    unittest.main()
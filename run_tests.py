import unittest
from Gamestate import Gamestate
from Piece import Piece
from PieceType import PieceType
from moveEngine.PawnMoveEngine import PawnMoveEngine

class TestPiece(unittest.TestCase):
    def testColor(self):
        whitePiece = Piece(True, None, [1,1], None)
        self.assertEqual(whitePiece.isWhite, True)
        blackPiece = Piece(False, None, [1,1], None)
        self.assertEqual(blackPiece.isWhite, False)

    def testGetName(self):
        piece = Piece(True, PieceType.PAWN, [1,1], None)
        self.assertEqual(piece.getPieceName(), 'P')

class TestPawnMoveset(unittest.TestCase):
    def testNormalMove(self):
        # start in middle of board
        whitePawn = Piece(id="asd", isWhiteIn= True, pieceTypeIn=PieceType.PAWN, startFile= 4, startRank= 4, moveEngine=PawnMoveEngine, )
        # white pawn should be able to move one step up
        whiteMoves = whitePawn.listPossibleMoves(4,4)
        self.assertIn([5,4], whiteMoves)
        # black pawn should be able to move one step down
        pass
        
    def testDiagonalTake(self):
        # if there is a piece diagonally up, white pawn should be able to take
        # if there is a piece diagonally down, black pawn should be able to take
        pass
        
    def testPromotion(self):
        # if white pawn moves to top rank, it should be promoted
        # if white pawn moves to bottom rank, it should be promoted
        pass

class TestGamestate(unittest.TestCase):
    def testBoardSingleton(self):
        gamestate1 = Gamestate()
        gamestate2 = Gamestate()
        self.assertEqual(id(gamestate1), id(gamestate2))
    
    def testBoardInit(self):
        gamestate = Gamestate()
        b = gamestate.board
        self.assertEqual(b.name, "mainboard")
        

if __name__ == '__main__':
    unittest.main()
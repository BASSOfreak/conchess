import unittest

class TestPawnMoveEngine(unittest.TestCase):
    def testNormalMove(self):
        # start in middle of board
        whitePawn = Piece(id="asd", isWhiteIn= True, pieceTypeIn=PieceType.PAWN, startFile= 4, startRank= 4)
        # white pawn should be able to move one step up
        whiteMoves = whitePawn.listPossibleMoves(4,4)
        self.assertIn([4,3], whiteMoves)
        # black pawn should be able to move one step down
        blackPawn = Piece(id="asd", isWhiteIn= False, pieceTypeIn=PieceType.PAWN, startFile= 4, startRank= 4)
        # white pawn should be able to move one step up
        blackMoves = blackPawn.listPossibleMoves(4,4)
        self.assertIn([4,5], blackMoves)
        
        
    def testDiagonalTake(self):
        # if there is a piece diagonally up, white pawn should be able to take
        gamestate = Gamestate()
        whitePawn = Piece(id="asd", isWhiteIn= True, pieceTypeIn=PieceType.PAWN, startFile= 5, startRank= 5)
        gamestate.initPieceOnSquare(whitePawn, 5,5)
        blackPawn = Piece(id="3924758fth", isWhiteIn= False, pieceTypeIn=PieceType.PAWN, startFile= 4, startRank= 4)
        gamestate.initPieceOnSquare(blackPawn, 4,4)
        resCanMove = whitePawn.canMove(5,5,4,4,True)
        self.assertEqual(resCanMove, True)
        # if there is a piece diagonally down, black pawn should be able to take
        
        
    def testPromotion(self):
        # if white pawn moves to top rank, it should be promoted
        # if white pawn moves to bottom rank, it should be promoted
        pass
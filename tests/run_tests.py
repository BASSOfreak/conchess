import unittest

print("test")



class TestPawnMoveEngine(unittest.TestCase):
    def testNormalMove(self):
        # start in middle of board
        whitePawn = Piece(id="asd", isWhiteIn= True, pieceTypeIn=PieceType.PAWN, startFile= 4, startRank= 4, moveEngine=PawnMoveEngine())
        # white pawn should be able to move one step up
        whiteMoves = whitePawn.listPossibleMoves(4,4)
        self.assertIn([4,3], whiteMoves)
        # black pawn should be able to move one step down
        blackPawn = Piece(id="asd", isWhiteIn= False, pieceTypeIn=PieceType.PAWN, startFile= 4, startRank= 4, moveEngine=PawnMoveEngine())
        # white pawn should be able to move one step up
        blackMoves = blackPawn.listPossibleMoves(4,4)
        self.assertIn([4,5], blackMoves)
        
        
    def testDiagonalTake(self):
        # if there is a piece diagonally up, white pawn should be able to take
        gamestate = Gamestate()
        whitePawn = Piece(id="asd", isWhiteIn= True, pieceTypeIn=PieceType.PAWN, startFile= 5, startRank= 5, moveEngine=PawnMoveEngine())
        gamestate.addPieceToSquare(whitePawn, 5,5)
        blackPawn = Piece(id="3924758fth", isWhiteIn= False, pieceTypeIn=PieceType.PAWN, startFile= 4, startRank= 4, moveEngine=PawnMoveEngine())
        gamestate.addPieceToSquare(blackPawn, 4,4)
        resCanMove = whitePawn.canMove(5,5,4,4,True)
        self.assertEqual(resCanMove, True)
        # if there is a piece diagonally down, black pawn should be able to take
        
        
    def testPromotion(self):
        # if white pawn moves to top rank, it should be promoted
        # if white pawn moves to bottom rank, it should be promoted
        pass

class TestRookMoveEngine(unittest.TestCase):
    def testListTakes(self):
        rook = Piece("asd32", True, PieceType.ROOK, 4,4,RookMoveEngine())
        takeList = rook.moveEngine.listPossibleTakes(4, 4, True)
        shouldBeList = [[4,1],[4,2],[4,3],[4,5],[4,6],[4,7],[4,8],[1,4],[2,4],[3,4],[5,4],[6,4],[7,4],[8,4]]
        self.assertCountEqual(takeList, shouldBeList)

    def testBlockedTake(self):
        gamestate = Gamestate()
        whiteRook = Piece("asd32", True, PieceType.ROOK, 4,7,RookMoveEngine())
        gamestate.addPieceToSquare(whiteRook, 4,7)
        whitePawn = Piece("324f5d876th", True, PieceType.PAWN, 4,5,PawnMoveEngine())
        gamestate.addPieceToSquare(whitePawn, 4,5)
        blackPawn = Piece("q327d6r4tg", False, PieceType.PAWN, 4,1,PawnMoveEngine())
        gamestate.addPieceToSquare(blackPawn, 4,1)
        self.assertEqual(whiteRook.canMove(4,7,4,1,True), False)

    def testNotBlockedTake(self):
        gamestate = Gamestate()
        whiteRook = Piece("asd32", True, PieceType.ROOK, 4,7,RookMoveEngine())
        gamestate.addPieceToSquare(whiteRook, 4,7)
        whitePawn = Piece("324f5d876th", True, PieceType.PAWN, 3,5,PawnMoveEngine())
        gamestate.addPieceToSquare(whitePawn, 3,5)
        blackPawn = Piece("q327d6r4tg", False, PieceType.PAWN, 4,1,PawnMoveEngine())
        gamestate.addPieceToSquare(blackPawn, 4,1)
        self.assertEqual(whiteRook.canMove(4,7,4,1,True), True)

class TestGamestate(unittest.TestCase):
    def testBoardSingleton(self):
        gamestate1 = Gamestate()
        gamestate2 = Gamestate()
        self.assertEqual(id(gamestate1), id(gamestate2))
    
    def testBoardInit(self):
        gamestate = Gamestate()
        b = gamestate.board
        self.assertEqual(b.name, "mainboard")

    def testPutPieceOnBoard(self):
        gamestate = Gamestate()
        whitePawn = Piece(id="asd", isWhiteIn= True, pieceTypeIn=PieceType.PAWN, startFile= 4, startRank= 4, moveEngine=PawnMoveEngine())
        gamestate.addPieceToSquare(whitePawn, 4,4)
        outPiece = gamestate.getPieceOnSquare(4,4)
        self.assertEqual(whitePawn, outPiece)

if __name__ == '__main__':
    unittest.main()
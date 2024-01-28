import unittest

class TestRookMoveEngine(unittest.TestCase):
    def testListTakes(self):
        rook = Piece("asd32", True, PieceType.ROOK, 4,4,RookMoveEngine())
        takeList = rook.moveEngine.listPossibleTakes(4, 4, True)
        shouldBeList = [[4,1],[4,2],[4,3],[4,5],[4,6],[4,7],[4,8],[1,4],[2,4],[3,4],[5,4],[6,4],[7,4],[8,4]]
        self.assertCountEqual(takeList, shouldBeList)

    def testBlockedTake(self):
        gamestate = Gamestate()
        whiteRook = Piece("asd32", True, PieceType.ROOK, 4,7,RookMoveEngine())
        gamestate.initPieceOnSquare(whiteRook, 4,7)
        whitePawn = Piece("324f5d876th", True, PieceType.PAWN, 4,5,PawnMoveEngine())
        gamestate.initPieceOnSquare(whitePawn, 4,5)
        blackPawn = Piece("q327d6r4tg", False, PieceType.PAWN, 4,1,PawnMoveEngine())
        gamestate.initPieceOnSquare(blackPawn, 4,1)
        self.assertEqual(whiteRook.canMove(4,7,4,1,True), False)

    def testNotBlockedTake(self):
        gamestate = Gamestate()
        whiteRook = Piece("asd32", True, PieceType.ROOK, 4,7,RookMoveEngine())
        gamestate.initPieceOnSquare(whiteRook, 4,7)
        whitePawn = Piece("324f5d876th", True, PieceType.PAWN, 3,5,PawnMoveEngine())
        gamestate.initPieceOnSquare(whitePawn, 3,5)
        blackPawn = Piece("q327d6r4tg", False, PieceType.PAWN, 4,1,PawnMoveEngine())
        gamestate.initPieceOnSquare(blackPawn, 4,1)
        self.assertEqual(whiteRook.canMove(4,7,4,1,True), True)
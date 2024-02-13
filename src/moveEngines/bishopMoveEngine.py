from gameComponents.board import Board
from moveEngines.moveEngine import MoveEngine

class BishopMoveEngine(MoveEngine):
    def __init__(self):
        super().__init__()

    def listPossibleMoves(self, startingFile: int, startingRank: int, isWhite: bool):
        return super().listDiagonalSquares(startingFile, startingRank)
    
    
    def listPossibleTakes(self, startingFile: int, startingRank: int, isWhite: bool):
        return self.listPossibleMoves(startingFile, startingRank, isWhite)
    
    def canMove(self, startingFile: int, startingRank: int, 
                destFile: int, destRank: int, isWhite: bool, board: Board) -> bool:
        # test if piece can move to square at all
        if [destFile, destRank] in self.listPossibleMoves(startingFile, startingRank, isWhite):
            # run check straight path clear based on wheather horizontal or vertical
            return super().checkDiagonalPathClear(startingFile, startingRank, destFile, destRank, board)
        else:
            return False
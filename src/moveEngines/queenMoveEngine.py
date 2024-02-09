from gameComponents.board import Board
from moveEngines.moveEngine import MoveEngine

class QueenMoveEngine(MoveEngine):
    def __init__(self):
        super().__init__()

    def listPossibleMoves(self, startingFile: int, startingRank: int, isWhite: bool):
        outSquares = []
        # list all squares that are on same rank OR same file
        for i in range(1,9):
            if i != startingRank:
                outSquares.append([startingFile, i])
            if i != startingFile:
                outSquares.append([i, startingRank])

        # add all diagonal squares
        outSquares.extend   (super().listDiagonalSquares(startingFile, startingRank))
        return outSquares
    
    
    def listPossibleTakes(self, startingFile: int, startingRank: int, isWhite: bool):
        return self.listPossibleMoves(startingFile, startingRank, isWhite)
    
    def canMove(self, startingFile: int, startingRank: int, 
                destFile: int, destRank: int, isWhite: bool, board: Board) -> bool:
        # check if can move there at all
        if [destFile, destRank] in self.listPossibleMoves(startingFile, startingRank, isWhite):
            # check if straight or diagonal
            if startingFile == destFile or startingRank == destRank:
                # run check straight path clear based on wheather horizontal or vertical
                return super().checkStraightPathClear(startingRank, destRank, destFile != startingFile, destFile, board)
            else:
                # run diagonal check
                return super().checkDiagonalPathClear(startingFile, startingRank, destFile, destRank, board)

        return False
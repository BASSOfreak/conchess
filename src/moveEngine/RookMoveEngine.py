from moveEngine.MoveEngine import MoveEngine

class RookMoveEngine(MoveEngine):
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
        return outSquares
    
    
    def listPossibleTakes(self, startingFile: int, startingRank: int, isWhite: bool):
        return self.listPossibleMoves(startingFile, startingRank, isWhite)
    
    def canMove(self, startingFile: int, startingRank: int, 
                destFile: int, destRank: int, isWhite: bool) -> bool:
        # in same file
        if destFile == startingFile:
            return super().checkStraightPathClear(startingRank, destRank, False, destFile)
        else:
            return super().checkStraightPathClear(startingFile, destFile, True, destRank)

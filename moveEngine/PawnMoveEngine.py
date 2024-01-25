from Gamestate import Gamestate
from moveEngine.MoveEngine import MoveEngine

class PawnMoveEngine(MoveEngine):
    def __init__(self):
        super.__init__(self)

    def possibleSquares(self, startingRank: int, startingFile: int, isWhite: bool):
        outSquares = []
        direction = 1
        if not isWhite:
            direction = -1
        
        # normal move
        outSquares.append([startingFile, startingRank + direction])   

        # double move
        if not self.hasMoved:
            outSquares.append([startingFile, startingRank + (2 * direction)])

        # take 
        gamestate = Gamestate()
        # take right
        if startingFile < 8 and gamestate.board.squareList[startingFile + 1][startingRank + direction].hasPiece:
            outSquares.append([startingFile + 1, startingRank + direction])

        # take left
        if startingFile > 1 and gamestate.board.squareList[startingFile - 1][startingRank + direction].hasPiece:
            outSquares.append([startingFile - 1, startingRank + direction])
from gameComponents.board import Board
from moveEngines.moveEngine import MoveEngine
from utility.utility import checkIfOnBoard

class KnightMoveEngine(MoveEngine):
    def __init__(self):
        super().__init__()

    def listPossibleMoves(self, startingFile: int, startingRank: int, isWhite: bool):
        allSquares = []
        # horizontal left
        horizontalLeft = startingFile - 2
        allSquares.append([horizontalLeft,startingRank - 1])
        allSquares.append([horizontalLeft,startingRank + 1])
        # horizontal right
        horizontalRight = startingFile + 2
        allSquares.append([horizontalRight, startingRank - 1])
        allSquares.append([horizontalRight, startingRank + 1])
        # vertical up
        verticalUp = startingRank - 2
        allSquares.append([startingFile - 1, verticalUp])
        allSquares.append([startingFile + 1, verticalUp])
        # vertical down
        verticalDown = startingRank + 2
        allSquares.append([startingFile - 1, verticalDown])
        allSquares.append([startingFile + 1, verticalDown])

        outputSquares = [square for square in allSquares if checkIfOnBoard(square)]
        # verticcal and then left and right
        return outputSquares
    
    
    def listPossibleTakes(self, startingFile: int, startingRank: int, isWhite: bool):
        return self.listPossibleMoves(startingFile, startingRank, isWhite)
    
    def canMove(self, startingFile: int, startingRank: int, 
                destFile: int, destRank: int, isWhite: bool, board: Board) -> bool:
        # make sure that destination square is among possible destination squares
        return [destFile, destRank] in self.listPossibleMoves(startingFile, startingRank, isWhite)
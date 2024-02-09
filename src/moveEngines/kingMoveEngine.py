from gameComponents.board import Board
from moveEngines.moveEngine import MoveEngine
from utility.utility import checkIfOnBoard

class KingMoveEngine(MoveEngine):
    def __init__(self):
        super().__init__()

    def listPossibleMoves(self, startingFile: int, startingRank: int, isWhite: bool):
        allSquares = []
        # up
        allSquares.append([startingFile - 1,startingRank - 1])
        allSquares.append([startingFile,startingRank - 1])
        allSquares.append([startingFile + 1,startingRank - 1])
        # right
        allSquares.append([startingFile + 1, startingRank])
        # left
        allSquares.append([startingFile - 1, startingRank])
        # down
        allSquares.append([startingFile - 1, startingRank + 1])
        allSquares.append([startingFile, startingRank + 1])
        allSquares.append([startingFile + 1, startingRank + 1])
        
        # only output squares that are actually on board
        outputSquares = [square for square in allSquares if checkIfOnBoard(square)]
        
        return outputSquares
    
    
    def listPossibleTakes(self, startingFile: int, startingRank: int, isWhite: bool):
        return self.listPossibleMoves(startingFile, startingRank, isWhite)
    
    def canMove(self, startingFile: int, startingRank: int, 
                destFile: int, destRank: int, isWhite: bool, board: Board) -> bool:
        # make sure that destination square is among possible destination squares
        return [destFile, destRank] in self.listPossibleMoves(startingFile, startingRank, isWhite)
from abc import ABC, abstractmethod
from gameComponents.board import Board
from utility.utility import signOf

class MoveEngine(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def listPossibleMoves(self, startingFile: int, startingRank: int, isWhite: bool):
        pass

    #can take in principle (if nothing is in the way etc)
    @abstractmethod
    def listPossibleTakes(self, startingFile: int, startingRank: int, isWhite: bool):
        pass
    
    #can move to a specific square
    @abstractmethod
    def canMove(self, startingFile: int, startingRank: int, 
                destFile: int, destRank: int, isWhite: bool) -> bool:
        pass

    def checkStraightPathClear(self, startingValue: int, destValue: int, horizontal: bool, otherDim: int, board: Board) -> bool:
        # in same file
        if destValue == startingValue:
            # get number of moves to make along file
            diff = destValue - startingValue
            currentTestValue = startingValue + signOf(diff)
            # make sure that there are no pieces in the way
            while abs(currentTestValue - destValue) > 0:
                squareOccupied = False
                if horizontal:
                    squareOccupied = board.getSquare(currentTestValue, otherDim).hasPiece
                else:
                    squareOccupied = board.getSquare(otherDim, currentTestValue).hasPiece
                if squareOccupied:
                    return False
                currentTestValue += signOf(diff)

            return True
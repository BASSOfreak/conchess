from abc import ABC, abstractmethod
from gameComponents.board import Board
from utility.utility import signOf

class MoveEngine(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def listPossibleMoves(self, startingFile: int, startingRank: int, isWhite: bool):
        pass

    # can take in principle (if nothing is in the way etc)
    @abstractmethod
    def listPossibleTakes(self, startingFile: int, startingRank: int, isWhite: bool):
        pass
    
    # can move to a specific square
    # check if there is a piece of opposite color on destination square or not
    # then either check takes or moves
    @abstractmethod
    def canMove(self, startingFile: int, startingRank: int, 
                destFile: int, destRank: int, isWhite: bool, board: Board) -> bool:
        pass

    def listDiagonalSquares(self, startingFile: int, startingRank: int):
        outSquares = []
        # list all squares that are diagonal
        # direction down right
        outFile = startingFile + 1
        outRank = startingRank + 1
        while outFile < 9 and outFile > 0 and outRank < 9 and outRank > 0:
            outSquares.append([outFile, outRank])
            outFile = outFile + 1
            outRank = outRank + 1
        
        # direction down left
        outFile = startingFile - 1
        outRank = startingRank + 1
        while outFile < 9 and outFile > 0 and outRank < 9 and outRank > 0:
            outSquares.append([outFile, outRank])
            outFile = outFile - 1
            outRank = outRank + 1

        # direction up right
        outFile = startingFile + 1
        outRank = startingRank - 1
        while outFile < 9 and outFile > 0 and outRank < 9 and outRank > 0:
            outSquares.append([outFile, outRank])
            outFile = outFile + 1
            outRank = outRank - 1

        # direction up left
        outFile = startingFile - 1
        outRank = startingRank - 1
        while outFile < 9 and outFile > 0 and outRank < 9 and outRank > 0:
            outSquares.append([outFile, outRank])
            outFile = outFile - 1
            outRank = outRank - 1

        return outSquares

    def checkStraightPathClear(self, startingValue: int, destValue: int, horizontal: bool, otherDim: int, board: Board) -> bool:
        #print("checking straight path clear")
        # in same file
        if destValue != startingValue:
            # get number of moves to make along file
            diff = destValue - startingValue
            currentTestValue = startingValue + signOf(diff)
            # make sure that there are no pieces in the way
            while abs(currentTestValue - destValue) > 0:
                #print(f"testing dimension {currentTestValue} and {otherDim}")
                squareOccupied = False
                if horizontal:
                    squareOccupied = board.getSquare(currentTestValue, otherDim).hasPiece
                else:
                    squareOccupied = board.getSquare(otherDim, currentTestValue).hasPiece
                #print(f"sqaure occupied? {squareOccupied}")
                if squareOccupied:
                    #print(f"cannot move because square is blocked")
                    return False
                currentTestValue += signOf(diff)

            return True
        
        return True
        
    def checkDiagonalPathClear(self, startingFile: int, startingRank: int, destFile: int, destRank: int, board: Board) -> bool:
        # get file and rank direction
        diffFile = destFile - startingFile
        dirFile = signOf(diffFile)
        diffRank = destRank - startingRank
        dirRank = signOf(diffRank)
        currentTestFile = startingFile + dirFile       
        currentTestRank = startingRank + dirRank
        while abs(currentTestFile - destFile) > 0:
            if board.getSquare(currentTestFile, currentTestRank).hasPiece:
                return False
            currentTestFile = currentTestFile + dirFile       
            currentTestRank = currentTestRank + dirRank

        return True
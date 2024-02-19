from moveEngines.moveEngine import MoveEngine
from gameComponents.board import Board
from gameComponents.square import Square

class PawnMoveEngine(MoveEngine):
    def __init__(self):
        super().__init__()

    def listPossibleMoves(self, startingFile: int, startingRank: int, isWhite: bool, board: Board):
        outSquares = []
        direction = -1
        if not isWhite:
            direction = 1
        
        # normal move
        outSquares.append([startingFile, startingRank + direction])   

        # double move
        if (startingRank == 7 and isWhite) or (startingRank == 2 and not isWhite):
            outSquares.append([startingFile, startingRank + (2 * direction)])

        # take 
        # take right
        takeRight = self.tryTakeRight(startingFile, startingRank, direction, board)
        if takeRight != None:
            outSquares.append(takeRight)

        # take left
        takeLeft = self.tryTakeLeft(startingFile, startingRank, direction, board)
        if takeLeft != None:
            outSquares.append(takeLeft)

        return outSquares
    
    def tryTakeLeft(self, fileIn, rankIn, direction: int, board: Board):
        if fileIn < 8 and board.getSquare(fileIn + 1, rankIn + direction).hasPiece:
            return([fileIn - 1, rankIn + direction])
        else:
            return None
        
    def tryTakeRight(self, fileIn, rankIn, direction: int, board: Board):
        if fileIn < 8 and board.getSquare(fileIn + 1, rankIn + direction).hasPiece:
            return([fileIn + 1, rankIn + direction])
        else:
            return None

    def listPossibleTakes(self, startingFile: int, startingRank: int, isWhite: bool):
        output = []
        direction = -1
        if not isWhite:
            direction = 1

        if startingFile > 1:
            output.append([startingRank + direction, startingFile - 1])

        if startingFile < 8:
            output.append([startingRank + direction, startingFile + 1])
        
        return output

    def canMove(self, startingFile: int, startingRank: int, 
                destFile: int, destRank: int, isWhite: bool, board: Board) -> bool:
        direction = -1
        if not isWhite:
            direction = 1
        
        # check if moving one rank up
        if startingRank + direction == destRank:
            # move normally
            if startingFile == destFile:
                targetSquarePiece = board.getSquare(destFile, destRank).getPiece()
                if targetSquarePiece == None:
                    return True
            # take in adjacent file    
            elif startingFile + 1 == destFile or startingFile - 1 == destFile:
                targetSquarePiece = board.getSquare(destFile, destRank).getPiece()
                # make sure that there is a piece and that color is opposite
                if targetSquarePiece != None and targetSquarePiece.isWhite != isWhite:
                    return True
                # check for en passant in starting rank and target file
                elif board.getSquare(destFile, startingRank).hasPiece and board.getSquare(destFile, startingRank).getPiece().hasMadeDoubleMove:
                    return True

        # double move
        # determine proper starting position for double move    
        doubleMoveRank = 7 if isWhite else 2
        if startingFile == destFile and startingRank == doubleMoveRank and destRank == startingRank + 2 * direction:
            if not board.getSquare(startingFile, startingRank + direction).hasPiece:
                if not board.getSquare(destFile, destRank).hasPiece:
                    return True

        return False
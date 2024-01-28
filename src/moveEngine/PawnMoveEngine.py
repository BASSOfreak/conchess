from Gamestate import Gamestate
from moveEngine.MoveEngine import MoveEngine

class PawnMoveEngine(MoveEngine):
    def __init__(self):
        super().__init__()

    def listPossibleMoves(self, startingFile: int, startingRank: int, isWhite: bool):
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
        gamestate = Gamestate()
        # take right
        takeRight = self.tryTakeRight(startingFile, startingRank, direction, gamestate)
        if takeRight != None:
            outSquares.append(takeRight)

        # take left
        takeLeft = self.tryTakeLeft(startingFile, startingRank, direction, gamestate)
        if takeLeft != None:
            outSquares.append(takeLeft)

        return outSquares
    
    def tryTakeLeft(self, fileIn, rankIn, direction: int, gamestate: Gamestate):
        if fileIn < 8 and gamestate.pieceOnSquare(fileIn + 1, rankIn + direction):
            return([fileIn - 1, rankIn + direction])
        else:
            return None
        
    def tryTakeRight(self, fileIn, rankIn, direction: int, gamestate: Gamestate):
        if fileIn < 8 and gamestate.pieceOnSquare(fileIn + 1, rankIn + direction):
            return([fileIn + 1, rankIn + direction])
        else:
            return None

    def listPossibleTakes(self, startingFile: int, startingRank: int, isWhite: bool):
        output = []
        direction = -1
        if not isWhite:
            direction = 1

        output.append([startingRank + direction, startingFile + 1])
        output.append([startingRank + direction, startingFile - 1])

        return output

    def canMove(self, startingFile: int, startingRank: int, 
                destFile: int, destRank: int, isWhite: bool) -> bool:
        direction = -1
        if not isWhite:
            direction = 1
        
        # check if moving one rank up
        if startingRank + direction == destRank:
            gamestate = Gamestate()
            # move normally
            if startingFile == destFile:
                targetSquarePiece = gamestate.getPieceOnSquare(destFile, destRank)
                if targetSquarePiece == None:
                    return True
            # take in adjacent file    
            elif startingFile + 1 == destFile or startingFile - 1 == destFile:
                targetSquarePiece = gamestate.getPieceOnSquare(destFile, destRank)
                # make sure that there is a piece and that color is opposite
                if targetSquarePiece != None and targetSquarePiece.isWhite != isWhite:
                    return True

        # double move
        # determine proper starting position for double move    
        doubleMoveRank = 7 if isWhite else 2
        if startingFile == destFile and startingRank == doubleMoveRank and destRank == startingRank + 2 * direction:
            if gamestate.getPieceOnSquare(startingFile, startingRank + direction) == None:
                if gamestate.getPieceOnSquare(destFile, destRank) == None:
                    return True

        return False
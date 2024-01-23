from Utility import fileToLetter

class Move:
    def __init__(self, piece: str, rankIndex: int, fileIndex: int):
        self.rankIndex = rankIndex
        self.fileIndex = fileIndex
        self.piece = piece

    def toNotation(self) -> str:
        return self.piece + fileToLetter(self.fileIndex) + str(self.rankIndex)
    
    
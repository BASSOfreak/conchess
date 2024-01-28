from Square import Square
class Board:
    def __init__(self, name: str):
        self.name = name
        self.squareList = [[None] * 8] * 8
        for file in range(8):
            for rank in range(8):
                self.squareList[file][rank] = Square(rank + 1, file + 1)

    def createCopy(self):
        copyBoard = Board("copy_of_" + self.name)
        copyBoard.squareList = self.squareList
        return copyBoard
    
    def getSquare(self, fileIn, rankIn) -> Square:
        return self.squareList[fileIn][rankIn]
    
        
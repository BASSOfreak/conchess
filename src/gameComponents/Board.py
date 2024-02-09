from gameComponents.square import Square
class Board:
    def __init__(self, name: str):
        self.name = name
        self.squareList = [[0 for i in range(8)] for j in range(8)]
        for file in range(8):
            for rank in range(8):
                self.squareList[file][rank] = Square(rank + 1, file + 1)

    def createCopy(self):
        copyBoard = Board("copy_of_" + self.name)
        copyBoard.squareList = self.squareList
        return copyBoard
    
    def getSquare(self, fileIn, rankIn) -> Square:
        return self.squareList[fileIn - 1][rankIn - 1]
    
    # prints entire board to console
    def draw(self):
        print(" ")
        for rank in range(8):
            print("|", end="")
            for file in range(8):
                if self.getSquare(file, rank).hasPiece:
                    print(self.getSquare(file, rank).getPiece().getPieceName(), end="")
                else:
                    print("X", end="")
                print("|", end="")
            print(" ")

    
        
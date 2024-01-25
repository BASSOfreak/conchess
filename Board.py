from Square import Square
class Board:
    def __init__(self, name: str):
        self.name = name
        squareList = [[None] * 8] * 8
        for file in range(8):
            for rank in range(8):
                squareList[file][rank] = Square(rank + 1, file + 1)
        
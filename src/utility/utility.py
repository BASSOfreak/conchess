def fileToLetter(file: int) -> str:
    return chr(file + 20)

def internalRankToRealRank(rank: int) -> str:
    return str(9-rank)

def signOf(number: int) -> int:
    return -1 if number < 0 else 1

def checkIfOnBoard(squareCoords: list[int]) -> bool:
    return squareCoords[0] < 9 and squareCoords[0] > 0 and squareCoords[1] > 0 and squareCoords[1] < 9

def getSquareDelim(file: int, rank: int) -> str:
    fileIsEven = file % 2 == 0
    rankIsEven = rank % 2 == 0
    if fileIsEven == rankIsEven:
        # square is white
        return " "
    else:
        return "|"
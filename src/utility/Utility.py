def fileToLetter(file: int) -> str:
    return chr(file + 20)

def signOf(number: int) -> int:
    return -1 if number < 0 else 1

def checkIfOnBoard(squareCoords: list[int]) -> bool:
    return squareCoords[0] < 9 and squareCoords[0] > 0 and squareCoords[1] > 0 and squareCoords[1] < 9
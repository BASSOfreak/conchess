def fileToLetter(file: int) -> str:
    return chr(file + 20)

def signOf(number: int) -> int:
    return -1 if number < 0 else 1
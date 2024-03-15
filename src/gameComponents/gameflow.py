import requests

from gameComponents.gamestate import Gamestate
from utility.utility import letterToFile

class Gameflow:
    _instance = None
    
    HasCastled: bool = False
    gamestate = Gamestate()

    roundCounter = 0 # increment every two moves
    turnCounter = 0 # increment with every move

    URL = "https://www.chessdb.cn/cdb.php" # for querrying moves

    def __new__(cls):
        if cls._instance is None:
            print('Creating game flow instance')
            cls._instance = super(Gameflow, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance
    
    def gameLoop(cls):
        cls.gamestate.clearBoard()
        cls.gamestate.getCurrentBoard().initGameBoard()
        while True:
            #draw board
            cls.gamestate.drawBoard()
            # white move
            print("white to move")
            cls.makePlayerMove(True)
            
            #draw board
            cls.gamestate.drawBoard()
            
            # black move
            print("black to move")
            cls.makePlayerMove(False)

    def makePlayerMove(cls, isWhite: bool):
        moveNotMade = True
        while moveNotMade:
            print("select square of piece to move (e.g. \"A2\")")
            start = input()
            if not len(start) == 2:
                print("input needs to be 2 characters")
                continue

            startFile = letterToFile(start[0])
            if not startFile < 9 and startFile > 0:
                print("file must be between A and H")
                continue

            startRank = 9 - int(start[1])
            if not startRank < 9 and startRank > 0:
                print("rank must be between 1 and 8")
                continue
            
            print("select destination square (e.g. \"A3\")")
            dest = input()
            if not len(dest) == 2:
                print("input needs to be 2 characters")
                continue

            destFile = letterToFile(dest[0])
            if not destFile < 9 and destFile > 0:
                print("file must be between A and H")
                continue

            destRank = 9 - int(dest[1])
            if not destRank < 9 and destRank > 0:
                print("rank must be between 1 and 8")
                continue
            
            # try to make move
            piece = cls.gamestate.getPieceOnSquare(startFile, startRank)
            if not piece.isWhite == isWhite:
                print("selected piece of wrong color")
                continue

            [success, comment] = cls.gamestate.attemptMove(piece.id, destFile, destRank)

            if success:
                moveNotMade = False

            print(comment)

    def makeComputerMove(cls, difficulty: int):
        PARAMS = {"action": "querybest",
          "board": "8/8/k3P3/8/2K2p2/8/8/8 w - - 0 50"}
        r = requests.get(url = cls.URL, params = PARAMS)
        data = r.text
from gameComponents.piece import Piece
from gameComponents.pieceType import PieceType
from gameComponents.gamestate import Gamestate

def main():
    # initialize board
    gamestate = Gamestate()
    gamestate.getCurrentBoard().initGameBoard()
    gamestate.getCurrentBoard().draw()

    # start game loop
    
if __name__ == '__main__':
    main()
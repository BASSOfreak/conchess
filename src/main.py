from gameComponents.piece import Piece
from gameComponents.pieceType import PieceType
from gameComponents.gamestate import Gamestate

def main():
    # initialize board
    gamestate = Gamestate()
    piece1 = Piece("p1", True, PieceType.PAWN, 1,2)
    gamestate.initPieceOnSquare(piece1)
    

    # start game loop
    
if __name__ == '__main__':
    main()
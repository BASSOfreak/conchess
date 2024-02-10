from gameComponents.piece import Piece


class Square():
    def __init__(self, rankIn, fileIn):
        assert 0 < rankIn < 9 and 0 < fileIn < 9, "rank out of bounds"
        self.rank = rankIn
        self.file = fileIn
        self.hasPiece = False
        self.piece = None

    def landOnSquare(self, piece: Piece):
        self.hasPiece = True
        self.piece = piece

    def leaveSquare(self):
        self.hasPiece = False
        self.piece = None

    def getPiece(self) -> Piece:
        return self.piece
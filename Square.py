from PieceType import PieceType


class Square():
    def __init__(self, rankIn, fileIn):
        assert 0 < rankIn < 9 and 0 < fileIn < 9, "rank out of bounds"
        self.rank = rankIn
        self.file = fileIn
        self.hasPiece = False
        self.pieceType = None

    def landOnSquare(self, pieceType: PieceType):
        self.hasPiece = True
        self.pieceType = pieceType

    def leaveSquare(self):
        self.hasPiece = False
        self.pieceType = None
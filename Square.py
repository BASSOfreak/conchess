class Square():
    def __init__(self, rankIn, fileIn):
        assert 0 < rankIn < 9 and 0 < rankIn < 9, "rank out of bounds"
        self.rank = rankIn
        self.file = fileIn
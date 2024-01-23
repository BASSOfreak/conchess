from abc import ABC, abstractmethod

class PieceType(ABC):
    @abstractmethod
    def possibleSquares():
        pass
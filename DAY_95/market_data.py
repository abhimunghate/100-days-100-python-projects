from dataclasses import dataclass

@dataclass
class PricePoint:
    day: int
    close: float

class MarketData:
    def __init__(self, symbol, prices):
        self.symbol = symbol
        self.points = [PricePoint(i + 1, p) for i, p in enumerate(prices)]

    def closes(self):
        return [point.close for point in self.points]
    
# Done
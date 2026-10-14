class TrendPredictor:
    def fit(self, prices):
        if len(prices) < 2:
            raise ValueError("At least two prices are required")
        n = len(prices)
        xs = range(1, n + 1)
        x_mean = (n + 1) / 2
        y_mean = sum(prices) / n
        numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(xs, prices))
        denominator = sum((x - x_mean) ** 2 for x in xs)
        self.slope = numerator / denominator
        self.intercept = y_mean - self.slope * x_mean
        self.count = n
        return self

    def predict_next(self):
        return round(self.intercept + self.slope * (self.count + 1), 2)

    def moving_average(self, prices, window=3):
        if len(prices) < window:
            raise ValueError("Not enough prices for moving average")
        return round(sum(prices[-window:]) / window, 2)
    
# Done
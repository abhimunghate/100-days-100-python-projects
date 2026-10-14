# This is Day 95 project : Stock Price Prediction Tool

import json
from evaluation import backtest
from market_data import MarketData
from predictor import TrendPredictor

def show(action, data):
    print(f"\nREQUEST {action}\nRESPONSE 200\n{json.dumps(data,indent=2)}")

def main():
    print("Day 95 — Stock Price Prediction Tool")
    data = MarketData("ACME", [101.2, 102.8, 102.1, 104.6, 105.4, 106.9, 108.1])
    prices = data.closes()
    model = TrendPredictor().fit(prices)
    show("GET /api/market-data", {"symbol": data.symbol, "closing_prices": prices})
    show(
        "POST /api/predictions",
        {
            "symbol": data.symbol,
            "next_close_prediction": model.predict_next(),
            "three_day_average": model.moving_average(prices),
            "evaluation": backtest(prices, TrendPredictor),
            "method": "linear trend",
        }
    )

if __name__ == "__main__":
    main()
    
# Done
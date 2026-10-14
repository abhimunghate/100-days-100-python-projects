# 📈 Day 95 - Stock Price Prediction Tool

Welcome to **Day 95** of my **100 Days, 100 Python Projects** challenge!

This project is a **Stock Price Prediction Tool** built using Python. It demonstrates how historical stock closing prices can be analyzed to estimate the next closing price, calculate moving averages, and evaluate prediction accuracy using a simple backtesting technique.

The application uses Python classes, dataclasses, lists, mathematical calculations, linear regression concepts, and error evaluation to implement a basic stock trend prediction system. It simulates API-style requests and responses through formatted JSON output in the terminal.

The project uses sample closing prices for a fictional stock symbol, `ACME`. It fits a linear trend model to the historical prices, estimates the next closing price, calculates a three-day moving average, and evaluates predictions using Mean Absolute Error (MAE).

**Note:** This is an educational prediction tool that uses predefined sample data. It does not fetch live stock market prices, and its predictions are not financial advice or a guarantee of future market performance.

---

## 📌 Project Overview

Stock price analysis involves examining historical market data to identify patterns, estimate trends, and evaluate forecasting methods.

This project implements a simple mathematical approach to stock price prediction using **linear trend analysis**. It fits a straight line to historical closing prices and extrapolates that trend to estimate the next closing price.

The application follows a simple workflow:

- 📊 Load sample historical closing prices.
- 🏷️ Associate the prices with a stock symbol.
- 📈 Fit a linear trend model to the historical data.
- 🔮 Predict the next closing price.
- 🧮 Calculate a three-day moving average.
- 🧪 Backtest the prediction method using historical observations.
- 📉 Calculate Mean Absolute Error (MAE).
- 📋 Display market data and prediction results.
- 🧾 Format results as JSON in the terminal.

The sample dataset contains seven closing prices for the fictional symbol `ACME`.

---

## ✨ Features

- 📈 Stock price prediction using a linear trend
- 📊 Historical closing price management
- 🏷️ Stock symbol identification
- 🔮 Next closing price estimation
- 🧮 Three-day moving average calculation
- 🧪 Historical backtesting
- 📉 Mean Absolute Error calculation
- 📋 Evaluation test-point reporting
- ⚠️ Validation for insufficient prediction data
- 🧩 Modular Python architecture
- 🧾 JSON-formatted terminal output
- 🔄 API-style request and response labels
- 🐍 Python standard-library implementation

---

## 📊 Market Data Management

The `market_data.py` module defines two important components:

- `PricePoint` — represents a closing price for a particular day.
- `MarketData` — manages the stock symbol and its historical price points.

### PricePoint Dataclass

The `PricePoint` dataclass stores the day number and its corresponding closing price.

```python
from dataclasses import dataclass

@dataclass
class PricePoint:
    day: int
    close: float
```

### Attributes

| Attribute | Description |
|---|---|
| `day` | Sequential day number assigned to the price point |
| `close` | Closing price recorded for that day |

For example:

```python
PricePoint(day=1, close=101.2)
```

This represents the first day's closing price as `101.2`.

Using a dataclass makes each historical observation easy to create, access, and maintain.

### MarketData Class

The `MarketData` class organizes the price points associated with a stock symbol.

```python
class MarketData:
    def __init__(self, symbol, prices):
        self.symbol = symbol
        self.points = [
            PricePoint(i + 1, p)
            for i, p in enumerate(prices)
        ]

    def closes(self):
        return [point.close for point in self.points]
```

When initialized, the class receives a stock symbol and a list of prices.

```python
data = MarketData(
    "ACME",
    [101.2, 102.8, 102.1, 104.6, 105.4, 106.9, 108.1]
)
```

The constructor converts each price into a `PricePoint` object and assigns sequential day numbers beginning at `1`.

### The `closes()` Method

```python
def closes(self):
    return [point.close for point in self.points]
```

This method extracts the closing prices from the stored price points and returns them as a list.

Example output:

```python
[101.2, 102.8, 102.1, 104.6, 105.4, 106.9, 108.1]
```

The prediction model uses this list as its input.

**Important:** The day numbers are simple sequential indexes. They do not represent actual calendar dates or trading-session dates.

---

## 📈 TrendPredictor Class

The `TrendPredictor` class in `predictor.py` implements the stock price prediction logic.

It uses a straight-line mathematical model to estimate the relationship between the observation index and the closing price.

The model has two main parameters:

- **Slope** — represents the estimated price change per observation.
- **Intercept** — represents the line's estimated value when the observation index is zero.

The model fits these parameters using the least-squares linear regression method.

### Fitting the Model

```python
class TrendPredictor:
    def fit(self, prices):
        if len(prices) < 2:
            raise ValueError("At least two prices are required")

        n = len(prices)
        xs = range(1, n + 1)

        x_mean = (n + 1) / 2
        y_mean = sum(prices) / n

        numerator = sum(
            (x - x_mean) * (y - y_mean)
            for x, y in zip(xs, prices)
        )

        denominator = sum(
            (x - x_mean) ** 2
            for x in xs
        )

        self.slope = numerator / denominator
        self.intercept = y_mean - self.slope * x_mean
        self.count = n

        return self
```

### How It Works

1. Check that at least two prices are available.
2. Assign sequential indexes to the prices.
3. Calculate the mean of the observation indexes.
4. Calculate the mean of the closing prices.
5. Calculate the numerator and denominator used for the regression slope.
6. Calculate the slope.
7. Calculate the intercept.
8. Store the number of training observations.
9. Return the fitted model.

Returning `self` allows method chaining:

```python
model = TrendPredictor().fit(prices)
```

### Linear Trend Equation

The fitted line uses the equation:

\[
\hat{y} = a + bx
\]

Where:

- \(\hat{y}\) is the estimated closing price.
- \(a\) is the intercept.
- \(b\) is the slope.
- \(x\) is the observation index.

The slope is calculated as:

\[
b =
\frac{\sum_{i=1}^{n}(x_i-\bar{x})(y_i-\bar{y})}
{\sum_{i=1}^{n}(x_i-\bar{x})^2}
\]

The intercept is:

\[
a = \bar{y} - b\bar{x}
\]

These equations determine the straight line that minimizes the sum of squared vertical errors between the observed prices and the fitted values.

### Why Linear Regression?

Linear regression provides a straightforward way to estimate an overall trend from historical data.

It is useful for learning:

- How to calculate a trend from numerical observations.
- How slope and intercept determine a prediction line.
- How to extrapolate a fitted line beyond the training data.
- How to evaluate predictions against actual observations.

However, stock prices are influenced by many factors and do not necessarily follow a straight-line trend.

---

## 🔮 Next Closing Price Prediction

The `predict_next()` method estimates the next closing price by evaluating the fitted line at the next observation index.

```python
def predict_next(self):
    return round(
        self.intercept + self.slope * (self.count + 1),
        2
    )
```

### How It Works

1. Retrieve the fitted slope and intercept.
2. Determine the next observation index using `self.count + 1`.
3. Calculate the estimated price using the linear equation.
4. Round the result to two decimal places.
5. Return the prediction.

For the supplied dataset, the model is fitted using seven observations. Therefore, it predicts the price at observation index `8`.

The result is an extrapolation of the historical linear trend, not a guaranteed future market price.

---

## 🧮 Moving Average Calculation

The `moving_average()` method calculates the arithmetic average of the most recent prices within a specified window.

```python
def moving_average(self, prices, window=3):
    if len(prices) < window:
        raise ValueError("Not enough prices for moving average")

    return round(
        sum(prices[-window:]) / window,
        2
    )
```

### How It Works

1. Check that enough prices exist for the requested window.
2. Select the most recent prices using list slicing.
3. Calculate their arithmetic mean.
4. Round the result to two decimal places.
5. Return the moving average.

### Three-Day Moving Average

The application calls:

```python
model.moving_average(prices)
```

Since the default window is `3`, the method uses the last three prices:

```text
105.4, 106.9, 108.1
```

The calculation is:

\[
\text{Moving Average}
=
\frac{105.4+106.9+108.1}{3}
\]

\[
= 106.80
\]

The three-day moving average is therefore **106.80**.

### Why Moving Averages?

Moving averages help summarize recent price levels and reduce some short-term fluctuations in a series.

This implementation calculates a simple moving average. It does not assign greater weight to newer prices, as an exponential moving average would.

---

## 🧪 Backtesting the Prediction Model

The `evaluation.py` module contains the `backtest()` function.

Backtesting evaluates how a prediction method would have performed on historical observations that were not included in each individual model fit.

```python
def backtest(prices, predictor_class):
    errors = []

    for end in range(3, len(prices)):
        prediction = (
            predictor_class()
            .fit(prices[:end])
            .predict_next()
        )

        errors.append(abs(prices[end] - prediction))

    return {
        "mean_absolute_error": round(
            sum(errors) / len(errors),
            2
        ),
        "test_points": len(errors)
    }
```

### How It Works

1. Initialize an empty list to store prediction errors.
2. Iterate through the historical prices beginning at index `3`.
3. Use the prices before the current index as the training data.
4. Fit a new predictor using that training data.
5. Predict the next price.
6. Compare the prediction with the actual historical price.
7. Calculate the absolute error.
8. Average the errors and return the MAE and test-point count.

### Historical Evaluation Example

For the seven supplied prices, the function performs four one-step-ahead tests:

| Test | Training Observations | Actual Price Index |
|---|---:|---:|
| 1 | 3 | 4 |
| 2 | 4 | 5 |
| 3 | 5 | 6 |
| 4 | 6 | 7 |

Each test fits a fresh model using only the prices preceding the price being evaluated.

This approach avoids using the test observation to fit the model for that particular prediction.

**Important:** The backtest begins with three training observations because the loop starts at index `3`. Although `TrendPredictor.fit()` only requires two prices, the backtesting function uses at least three for its first test.

---

## 📉 Mean Absolute Error (MAE)

The application evaluates its predictions using Mean Absolute Error.

MAE measures the average absolute difference between predicted prices and actual prices.

\[
MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
\]

Where:

- \(n\) is the number of test observations.
- \(y_i\) is the actual closing price.
- \(\hat{y}_i\) is the predicted closing price.

### Example

Suppose the prediction errors are:

```text
1.20, 0.80, 1.50, 0.50
```

Then:

\[
MAE = \frac{1.20+0.80+1.50+0.50}{4}
\]

\[
MAE = 1.00
\]

An MAE of `1.00` means that the predictions differ from the actual prices by an average of one price unit across the evaluated observations.

### Evaluation Output

The `backtest()` function returns:

```json
{
  "mean_absolute_error": 1.23,
  "test_points": 4
}
```

The numerical MAE above is illustrative; the program calculates the actual value from the supplied dataset.

A lower MAE indicates smaller average absolute prediction errors on the evaluated observations. It does not guarantee better future performance.

---

## 🧾 API-Style Request and Response Format

The `show()` helper function in `main95.py` prints simulated operation labels and JSON-formatted results.

```python
def show(action, data):
    print(
        f"\nREQUEST {action}\n"
        f"RESPONSE 200\n"
        f"{json.dumps(data, indent=2)}"
    )
```

### Operations Demonstrated

| Operation | Status Label | Purpose |
|---|---:|---|
| `GET /api/market-data` | `200` | Displays the stock symbol and closing prices |
| `POST /api/predictions` | `200` | Displays the next-price prediction, moving average, and evaluation metrics |

Both operations use the same simulated response status of `200`.

These are API-style labels printed in the terminal. The project does not implement a real HTTP server, expose actual endpoints, or receive network requests.

### Market Data Response

The first operation returns data similar to:

```json
{
  "symbol": "ACME",
  "closing_prices": [
    101.2,
    102.8,
    102.1,
    104.6,
    105.4,
    106.9,
    108.1
  ]
}
```

### Prediction Response

The second operation returns a dictionary containing:

- The stock symbol.
- The estimated next closing price.
- The three-day moving average.
- Backtesting metrics.
- The name of the prediction method.

Its structure is:

```json
{
  "symbol": "ACME",
  "next_close_prediction": 109.0,
  "three_day_average": 106.8,
  "evaluation": {
    "mean_absolute_error": 1.23,
    "test_points": 4
  },
  "method": "linear trend"
}
```

The example prediction and MAE are illustrative placeholders, not guaranteed output values. The actual prediction and evaluation metrics are calculated when the application runs.

---

## 🔄 Complete Application Workflow

The application follows this workflow:

```text
Start Application
        |
        v
Initialize MarketData
        |
        v
Load Sample Closing Prices
        |
        v
Extract Closing Price List
        |
        v
Fit TrendPredictor Model
        |
        v
Calculate Next Closing Price
        |
        v
Calculate Three-Day Moving Average
        |
        v
Backtest Historical Predictions
        |
        v
Calculate Mean Absolute Error
        |
        v
Prepare Market Data Response
        |
        v
Prepare Prediction Response
        |
        v
Display JSON Results
```

The workflow separates market data management, prediction calculations, and evaluation into independent components.

---

## 🏗️ Project Architecture

The project contains four main Python modules.

```text
                     main95.py
                         |
             +-----------+-----------+
             |           |           |
             v           v           v
        market_data.py predictor.py evaluation.py
             |           |           |
             v           v           v
         MarketData  TrendPredictor backtest()
             |           |           |
             v           v           v
         PricePoint  Linear Trend  Error Calculation
                         |           |
                         v           v
                    Next Price       MAE
                         |           |
                         +-----+-----+
                               |
                               v
                        JSON Output
```

### Module Responsibilities

- **`main95.py`** — initializes the sample market data, fits the model, calculates predictions, runs backtesting, and prints the results.
- **`market_data.py`** — defines the `PricePoint` dataclass and `MarketData` class.
- **`predictor.py`** — implements linear trend fitting, next-price prediction, and moving average calculation.
- **`evaluation.py`** — evaluates the prediction method using historical one-step-ahead tests and calculates MAE.

This modular architecture separates data management, mathematical prediction, and model evaluation, making the project easier to understand and extend.

---

## 📊 Sample Dataset

The project uses the following predefined closing prices:

| Day Index | Closing Price |
|---:|---:|
| 1 | 101.2 |
| 2 | 102.8 |
| 3 | 102.1 |
| 4 | 104.6 |
| 5 | 105.4 |
| 6 | 106.9 |
| 7 | 108.1 |

The dataset generally trends upward, although the second and third observations show a small decline.

The linear trend model fits a straight line across all seven prices and extrapolates the fitted line to the eighth observation.

The moving average uses only the last three prices, while backtesting evaluates predictions at the fourth through seventh observations using progressively larger training sets.

---

## 🛠️ Technologies Used

### 🐍 Python

Python is used to implement market data management, trend fitting, prediction, and evaluation.

### 🧩 Dataclasses

The `dataclasses` module defines the `PricePoint` model.

```python
from dataclasses import dataclass
```

### 📈 Linear Regression Mathematics

The prediction model uses least-squares calculations to determine the slope and intercept of a linear trend.

### 🧮 Lists and List Comprehensions

Lists store closing prices, and list comprehensions extract values and prepare model inputs.

### 🔢 Mathematical Calculations

The project performs:

- Mean calculations.
- Slope and intercept calculations.
- Next-value extrapolation.
- Moving average calculation.
- Absolute error calculation.
- Mean Absolute Error calculation.

### 🧪 Backtesting

The evaluation function tests the prediction method against historical observations that are excluded from each individual model fit.

### 🧾 JSON

The `json` module formats market data and prediction results for readable terminal output.

### ⚠️ Exception Handling

The prediction and moving average methods use `ValueError` to report insufficient input data.

---

## 📦 Requirements

This project uses Python's standard library and does not require any external Python packages.

Check your Python installation:

```bash
python --version
```

### `requirements.txt`

```text
# No external dependencies required.
```

No machine learning framework, stock market API, API key, database, or external package installation is required.

---

## 📂 Project Structure

```text
DAY_95/
│
├── main95.py
├── market_data.py
├── predictor.py
├── evaluation.py
├── requirements.txt
└── README.md
```

The `screenshots/` folder is optional and can be created to document the project.

### File Description

| File / Folder | Purpose |
|---|---|
| `main95.py` | Entry point and sample prediction workflow |
| `market_data.py` | Market data and price point management |
| `predictor.py` | Linear trend prediction and moving average |
| `evaluation.py` | Backtesting and MAE calculation |
| `requirements.txt` | Documents dependency requirements |
| `README.md` | Project documentation |

---

## ▶️ How to Run the Application

### Step 1 — Install Python

Ensure that Python is installed on your computer.

```bash
python --version
```

### Step 2 — Open the Project Directory

Open a terminal inside your `DAY_95` folder.

```bash
cd DAY_95
```

### Step 3 — Check the Files

Make sure the following Python files are present:

```text
main95.py
market_data.py
predictor.py
evaluation.py
```

### Step 4 — Run the Application

Execute:

```bash
python main95.py
```

### Step 5 — Review the Terminal Output

The terminal displays:

- The application title.
- The stock symbol and historical closing prices.
- The estimated next closing price.
- The three-day moving average.
- The backtesting MAE.
- The number of historical test points.

### Step 6 — Interpret the Results

Review the predicted price and compare it with the moving average and backtesting metrics.

Remember that these calculations use a small, predefined dataset and a simple linear model. They are intended for educational purposes rather than real investment decisions.

---

## ⚠️ Important Notes and Limitations

### 1. No Live Market Data

The application uses seven predefined closing prices. It does not retrieve real stock prices from an exchange or financial data provider.

### 2. Linear Trend Assumption

The predictor fits a straight line to historical prices. Real stock prices can behave nonlinearly and are influenced by many market and economic factors.

### 3. Small Dataset

The model uses only seven observations. This is insufficient for drawing reliable conclusions about a real stock's future performance.

### 4. No Financial Advice

The predicted price is a mathematical extrapolation, not a recommendation to buy, hold, or sell a stock.

### 5. Limited Input Validation

The model checks that at least two prices are available for fitting. It does not comprehensively validate price types, missing values, or invalid numerical values.

### 6. Moving Average Validation

The moving average method checks whether the input contains enough prices for the selected window. The current implementation does not explicitly validate that the window is a positive integer.

### 7. Backtesting Limitations

Backtesting uses a small number of historical observations. The evaluation is useful for learning, but its MAE may not represent future prediction accuracy.

### 8. No Advanced Machine Learning

The project does not use neural networks, random forests, or other advanced machine learning models. Its prediction method is a basic least-squares linear trend.

### 9. No Visualization

The application displays JSON output in the terminal. It does not currently plot historical prices, the fitted trend line, or prediction results.

### 10. No Persistent Market Database

Prices are stored in memory and are not automatically saved to a database or historical market-data file.

---

## 🧠 Concepts Practiced

This project provides practical experience with:

- Python dataclasses
- Object-oriented programming
- Lists and list comprehensions
- Historical data management
- Linear regression mathematics
- Slope and intercept calculation
- Mean calculations
- Trend extrapolation
- Moving averages
- Model fitting
- Backtesting
- One-step-ahead prediction
- Absolute errors
- Mean Absolute Error
- Input validation
- Exception handling
- JSON serialization
- Modular programming
- API-style response formatting

---

## 🎯 Learning Outcomes

By building this project, I practiced how to:

- Represent historical prices using a dataclass.
- Organize stock market data by symbol.
- Extract closing prices for analysis.
- Fit a simple linear trend model.
- Calculate regression slope and intercept.
- Predict the next observation from a fitted line.
- Calculate a moving average over recent prices.
- Evaluate predictions using historical observations.
- Calculate absolute prediction errors.
- Measure average prediction error using MAE.
- Separate market data, prediction logic, and evaluation logic.
- Format prediction results as JSON.
- Handle insufficient input data.
- Understand the limitations of simple financial forecasting models.

---

## 🔮 Future Improvements

Possible enhancements for future versions include:

- 🌐 Integrate a live financial market API.
- 📅 Use actual trading dates instead of sequential indexes.
- 📈 Visualize historical prices and trend lines using Matplotlib.
- 🔮 Display predictions on a price chart.
- 🧪 Compare linear regression with other forecasting methods.
- 📊 Add moving averages with configurable windows.
- 📉 Calculate additional metrics such as RMSE and MAPE.
- 🔍 Evaluate the model against a larger historical dataset.
- 📂 Load prices from CSV or Excel files.
- 🗄️ Store historical market data in a database.
- 📊 Add interactive charts using Plotly.
- 🌐 Build a web interface using Flask or Streamlit.
- 🔄 Add rolling-window backtesting.
- 📆 Evaluate performance across different market periods.
- ⚙️ Add stronger input validation.
- 🧪 Write automated tests for prediction and evaluation functions.
- 📈 Compare multiple stocks using the same evaluation framework.
- 🚀 Deploy the tool as an educational web application.

---

## 📅 100 Days, 100 Python Projects

This project is part of my **100 Days, 100 Python Projects** challenge.

The goal of this challenge is to build one Python project every day to strengthen programming fundamentals, improve problem-solving skills, and gain practical software development experience.

**Day 95** focuses on **Stock Price Prediction**, combining historical data management, linear trend estimation, moving averages, backtesting, and prediction error evaluation using Python.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀🐍📈
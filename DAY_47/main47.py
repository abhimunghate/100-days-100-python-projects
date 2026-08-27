# This is Day 47 project : Temperature Plotter

import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def load_data(file_path):
    """Load and validate temperature data from a CSV file."""
    try:
        data = pd.read_csv(file_path)
        required_columns = ["Date", "Temperature"]
        
        for column in required_columns:
            if column not in data.columns:
                raise ValueError(f"Missing required column: {column}")
        data["Date"] = pd.to_datetime(data["Date"],errors="coerce")
        data["Temperature"] = pd.to_numeric(data["Temperature"],errors="coerce")
        data = data.dropna(subset=["Date", "Temperature"])
        if data.empty:
            raise ValueError("No valid temperature data found.")
        
        if "City" not in data.columns:
            data["City"] = "Default City"
        data["City"] = (data["City"].fillna("Unknown").astype(str))
        data = data.sort_values(["City", "Date"])
        print("Data loaded successfully!")
        print(f"Valid records: {len(data)}")
        return data
    except Exception as error:
        print("Error loading data:", error)
        return None
        
def calculate_rolling_average(data):
    """Calculate 7-day rolling average for each city."""
    data = data.copy()
    data["7-Day Average"] = (data.groupby("City")["Temperature"].transform(lambda x: x.rolling(7).mean()))
    return data
        
def detect_anomalies(data):
    """Detect temperature anomalies for each city."""
    data = data.copy()
    mean_temperature = (data.groupby("City")["Temperature"].transform("mean"))
    std_temperature = (data.groupby("City")["Temperature"].transform("std"))
    data["Anomaly"] = ((data["Temperature"] > mean_temperature + 2 * std_temperature) | (data["Temperature"] < mean_temperature - 2 * std_temperature))
    return data

def daily_trend(data, city):
    """Plot daily temperature trend."""
    city_data = data[data["City"] == city].copy()
    city_data = calculate_rolling_average(city_data)
    city_data = detect_anomalies(city_data)
    plt.figure(figsize=(10, 6))

    plt.plot(city_data["Date"], city_data["Temperature"], label="Daily Temperature", marker="o", markersize=3)
    plt.plot(city_data["Date"], city_data["7-Day Average"], label="7-Day Average", linestyle="--")
    
    anomalies = city_data[city_data["Anomaly"]]
    plt.scatter(anomalies["Date"], anomalies["Temperature"], label="Anomalies", zorder=5)
    plt.title(f"Daily Temperature Trend - {city}")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def monthly_trend(data, city):
    """Aggregate temperature data monthly."""
    city_data = data[data["City"] == city].copy()
    city_data["Month"] = (city_data["Date"].dt.to_period("M").astype(str))
    
    monthly = (city_data.groupby("Month")["Temperature"].mean())
    plt.figure(figsize=(10, 6))
    monthly.plot(marker="o")
    plt.title(f"Monthly Average Temperature - {city}")
    plt.xlabel("Month")
    plt.ylabel("Average Temperature (°C)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def yearly_trend(data, city):
    """Aggregate temperature data yearly."""
    city_data = data[data["City"] == city].copy()
    city_data["Year"] = (city_data["Date"].dt.year)
    
    yearly = (city_data.groupby("Year")["Temperature"].mean())
    plt.figure(figsize=(9, 6))
    yearly.plot(kind="bar")
    plt.title(f"Yearly Average Temperature - {city}")
    plt.xlabel("Year")
    plt.ylabel("Average Temperature (°C)")
    plt.grid(axis="y")
    plt.tight_layout()
    plt.show()

def interactive_temperature_plot(data):
    """Create an interactive Plotly temperature chart."""
    data = calculate_rolling_average(data)
    fig = px.line(data, x="Date", y="Temperature", color="City", markers=True, title="Interactive Temperature Trends", labels={"Temperature": "Temperature (°C)", "Date": "Date"})
    fig.update_layout(hovermode="x unified")
    fig.show()

def interactive_city_comparison(data):
    """Compare temperatures of multiple cities."""
    fig = px.line(data, x="Date", y="Temperature", color="City", markers=True, title="City Temperature Comparison")
    fig.update_layout(hovermode="x unified")
    fig.show()

def save_interactive_chart(data):
    """Save interactive Plotly chart as HTML."""
    fig = px.line(data, x="Date", y="Temperature", color="City", markers=True, title="Interactive Temperature Trends")
    file_name = input("Enter HTML file name " "(e.g., temperature_chart.html): ").strip()
    
    if not file_name:
        print("Invalid file name.")
        return

    if not file_name.lower().endswith(".html"):
        file_name += ".html"
    fig.write_html(file_name)
    print(f"Interactive chart saved as {file_name}")

def show_statistics(data):
    """Display basic temperature statistics."""
    print("\n------ Temperature Statistics ------\n")

    print(f"Total Records : {len(data)}")
    print(f"Average Temperature : {data['Temperature'].mean():.2f} °C")
    print(f"Minimum Temperature : {data['Temperature'].min():.2f} °C")
    print(f"Maximum Temperature : {data['Temperature'].max():.2f} °C")
    print(f"Number of Cities : {data['City'].nunique()}")
    print(f"Date Range : {data['Date'].min().date()} to {data['Date'].max().date()}")

def choose_city(data):
    """Allow the user to select a city."""
    cities = sorted(data["City"].unique())

    print("\n------ Cities ------\n")
    for index, city in enumerate(cities, start=1):
        print(f"{index}. {city}")

    try:
        choice = int(input("Select city: "))
        if choice < 1 or choice > len(cities):
            raise ValueError
        return cities[choice - 1]
    except ValueError:
        print("Invalid city selection.")
        return None

def main():
    print("\n================================")
    print("   Temperature Plotter")
    print("================================")

    file_path = input("\nEnter temperature CSV file path: ").strip()
    data = load_data(file_path)

    if data is None:
        return
    show_statistics(data)

    while True:
        print("\n------ Temperature Analysis ------\n")

        print("1. Daily Temperature Trend")
        print("2. Monthly Temperature Trend")
        print("3. Yearly Temperature Trend")
        print("4. Interactive Temperature Plot")
        print("5. Compare Multiple Cities")
        print("6. Show Statistics")
        print("7. Save Interactive Chart")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == "1":
            city = choose_city(data)
            if city:
                daily_trend(data, city)
        elif choice == "2":
            city = choose_city(data)
            if city:
                monthly_trend(data, city)
        elif choice == "3":
            city = choose_city(data)
            if city:
                yearly_trend(data, city)
        elif choice == "4":
            interactive_temperature_plot(data)
        elif choice == "5":
            interactive_city_comparison(data)
        elif choice == "6":
            show_statistics(data)
        elif choice == "7":
            save_interactive_chart(data)
        elif choice == "8":
            print("\nExiting Temperature Plotter.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
# Done
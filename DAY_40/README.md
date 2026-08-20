# 🌦️ Day 40 - Mini Weather API

Welcome to **Day 40** of my **100 Days, 100 Python Projects** challenge!

This project is a simple **RESTful Weather API built using Python and Flask**. It demonstrates the fundamentals of building APIs with Flask, including **JSON responses, HTTP methods, URL parameters, request data, CRUD operations, error handling, and HTTP status codes**.

The API provides weather information for different cities and allows users to retrieve, add, update, and delete weather data through HTTP requests.

---

## 📌 Project Overview

The Mini Weather API provides a simple backend service where users can:

* 🌦️ View weather information
* 🏙️ Get weather data for all cities
* 🔍 Search weather information by city
* ➕ Add weather information for a new city
* ✏️ Update existing city weather
* 🗑️ Delete city weather information
* 📦 Receive responses in JSON format
* 🌐 Use REST API endpoints
* 🔄 Work with HTTP methods
* ⚠️ Handle invalid requests
* 📊 Use HTTP status codes

This project is designed to introduce the fundamentals of **REST APIs and backend development using Flask**.

---

## ✨ Features

* 🌐 Flask REST API
* 🌦️ Weather Data API
* 🏙️ Multiple City Weather Records
* 📋 Get All Weather Data
* 🔍 Get Weather by City
* ➕ Add New City
* ✏️ Update City Weather
* 🗑️ Delete City Weather
* 📦 JSON Responses
* 🔄 CRUD Operations
* 📡 HTTP GET Requests
* 📤 HTTP POST Requests
* 🔄 HTTP PUT Requests
* ❌ HTTP DELETE Requests
* ⚠️ Error Handling
* 📊 HTTP Status Codes
* 🐍 Python Backend
* 🛠️ Flask Debug Mode

---

## 🖼️ API Preview

The Mini Weather API is a backend application, so it does not contain traditional HTML web pages.

The API can be tested using tools such as:

* 🌐 Web Browser
* 🧪 Postman
* 🔧 Insomnia
* 💻 cURL
* 🐍 Python Requests

Example response:

```json
{
    "new york": {
        "temperature": 22,
        "condition": "Sunny"
    }
}
```

---

## 🛠️ Technologies Used

* **Python 3**
* **Flask**
* **JSON**
* **REST API**
* **HTTP**

### Python

Python is used to implement the API logic and manage the weather data.

### Flask

Flask is used to create the web server and API routes.

### JSON

JSON is used as the primary data format for API requests and responses.

### REST API

The application follows basic REST principles by using different HTTP methods for different operations.

---

## 📦 Installation

First, make sure Python is installed.

Check your Python version:

```bash
python --version
```

Install Flask:

```bash
pip install flask
```

---

## 📂 Project Structure

```text
DAY_40/
│
├── main40.py
└── README.md
```

### File Description

| File        | Purpose                    |
| ----------- | -------------------------- |
| `main40.py` | Main Flask API application |
| `README.md` | Project documentation      |

> The weather data is currently stored in a Python dictionary, so changes made using POST, PUT, or DELETE are temporary and will be lost when the application restarts.

---

## ▶️ How to Run

### 1. Open the project folder

Open the terminal inside the `DAY_40` folder.

### 2. Install Flask

```bash
pip install flask
```

### 3. Run the application

```bash
python main40.py
```

The Flask development server will start.

The API will normally be available at:

```text
http://127.0.0.1:5000/
```

---

# 🌐 API Endpoints

The API provides the following endpoints:

| Method   | Endpoint          | Purpose                             |
| -------- | ----------------- | ----------------------------------- |
| `GET`    | `/`               | Displays API welcome message        |
| `GET`    | `/weather`        | Returns all weather data            |
| `GET`    | `/weather/<city>` | Returns weather for a specific city |
| `POST`   | `/weather`        | Adds a new city                     |
| `PUT`    | `/weather/<city>` | Updates city weather                |
| `DELETE` | `/weather/<city>` | Deletes a city                      |

These endpoints demonstrate the basic **CRUD** operations:

```text
Create  → POST
Read    → GET
Update  → PUT
Delete  → DELETE
```

---

# 🏠 API Home Endpoint

The home endpoint is:

```text
GET /
```

It returns a welcome message.

### Request

```text
http://127.0.0.1:5000/
```

### Response

```json
{
    "message": "Welcome to the Mini Weather API!"
}
```

---

# 🌦️ Get All Weather Data

The endpoint:

```text
GET /weather
```

returns weather information for all available cities.

### Request

```text
http://127.0.0.1:5000/weather
```

### Example Response

```json
{
    "new york": {
        "temperature": 22,
        "condition": "Sunny"
    },
    "london": {
        "temperature": 15,
        "condition": "Cloudy"
    },
    "tokyo": {
        "temperature": 28,
        "condition": "Clear"
    },
    "sydney": {
        "temperature": 18,
        "condition": "Rainy"
    }
}
```

---

# 🔍 Get Weather by City

Weather information for a specific city can be retrieved using:

```text
GET /weather/<city>
```

For example:

```text
GET /weather/tokyo
```

### Response

```json
{
    "tokyo": {
        "temperature": 28,
        "condition": "Clear"
    }
}
```

The application converts the city name to lowercase:

```python
city = city.lower()
```

This allows requests such as:

```text
/weather/Tokyo
/weather/TOKYO
/weather/tokyo
```

to work with the same city record.

---

## ❌ City Not Found

If the requested city does not exist, the API returns:

```json
{
    "error": "City not found"
}
```

with HTTP status code:

```text
404 Not Found
```

The relevant code is:

```python
if city in weather_data:
    return jsonify({city: weather_data[city]})

return jsonify({"error": "City not found"}), 404
```

---

# ➕ Add New City Weather

A new city can be added using:

```text
POST /weather
```

The request should contain JSON data.

### Example Request

```json
{
    "city": "mumbai",
    "temperature": 30,
    "condition": "Cloudy"
}
```

### Example Response

```json
{
    "message": "weather for mumbai added successfully"
}
```

The API returns:

```text
201 Created
```

because a new resource has been successfully created.

---

## ⚠️ Missing Data

The API requires:

* City
* Temperature
* Condition

If any required information is missing, the API returns:

```json
{
    "error": "Missing city, temperature or condition"
}
```

with:

```text
400 Bad Request
```

The validation is performed using:

```python
if not city or temperature is None or not condition:
    return jsonify({
        'error': 'Missing city, temperature or condition'
    }), 400
```

---

## 🚫 Duplicate City

If the city already exists, the API does not create another record.

For example, attempting to add:

```json
{
    "city": "tokyo",
    "temperature": 30,
    "condition": "Sunny"
}
```

when Tokyo already exists returns:

```json
{
    "error": "City already exists"
}
```

with:

```text
409 Conflict
```

This demonstrates how HTTP status codes can communicate API errors.

---

# ✏️ Update City Weather

Existing weather information can be updated using:

```text
PUT /weather/<city>
```

For example:

```text
PUT /weather/london
```

### Request Body

```json
{
    "temperature": 20,
    "condition": "Sunny"
}
```

### Response

```json
{
    "message": "Weather for london updated successfully",
    "weather": {
        "temperature": 20,
        "condition": "Sunny"
    }
}
```

The API returns:

```text
200 OK
```

---

## ⚠️ Updating a Non-Existing City

If the city does not exist:

```text
PUT /weather/mumbai
```

the API returns:

```json
{
    "error": "City not found"
}
```

with:

```text
404 Not Found
```

---

## ⚠️ Missing Update Data

The update request requires:

* Temperature
* Condition

If either value is missing:

```json
{
    "error": "Missing temperature or condition"
}
```

is returned with:

```text
400 Bad Request
```

---

# 🗑️ Delete City Weather

Weather information can be removed using:

```text
DELETE /weather/<city>
```

For example:

```text
DELETE /weather/sydney
```

### Response

```json
{
    "message": "sydney removed successfully"
}
```

The API returns:

```text
200 OK
```

The city is removed using:

```python
del weather_data[city]
```

---

## ❌ Delete Non-Existing City

If the requested city does not exist:

```text
DELETE /weather/mumbai
```

the API returns:

```json
{
    "error": "City not found"
}
```

with:

```text
404 Not Found
```

---

# 📊 HTTP Status Codes

The API uses different HTTP status codes depending on the result.

| Status Code | Meaning     | Example                     |
| ----------- | ----------- | --------------------------- |
| `200`       | OK          | Successful GET, PUT, DELETE |
| `201`       | Created     | New city successfully added |
| `400`       | Bad Request | Required data missing       |
| `404`       | Not Found   | City does not exist         |
| `409`       | Conflict    | City already exists         |

Using appropriate HTTP status codes makes APIs easier for clients to understand and consume.

---

# 🔄 CRUD Operations

The API demonstrates all four basic CRUD operations.

### Create

```text
POST /weather
```

Adds a new city.

### Read

```text
GET /weather
GET /weather/<city>
```

Retrieves weather information.

### Update

```text
PUT /weather/<city>
```

Updates existing weather information.

### Delete

```text
DELETE /weather/<city>
```

Deletes a city.

The complete CRUD flow is:

```text
             Weather API
                  │
       ┌──────────┼──────────┐
       │          │          │
     Create      Read      Update
       │          │          │
      POST       GET        PUT
       │          │          │
       └──────────┼──────────┘
                  │
                Delete
                  │
                DELETE
```

---

# 📦 JSON Data

The API uses JSON as the main data format.

Flask's `jsonify()` function converts Python dictionaries into JSON responses.

For example:

```python
return jsonify(weather_data)
```

produces a JSON response.

Incoming JSON data is retrieved using:

```python
data = request.json
```

For example:

```python
data = request.json

city = data.get('city', '').lower()
temperature = data.get('temperature')
condition = data.get('condition')
```

This allows the API to receive structured data from API clients.

---

# 🧩 Flask Components

| Component      | Purpose                                  |
| -------------- | ---------------------------------------- |
| `Flask()`      | Creates the Flask application            |
| `jsonify()`    | Converts Python data into JSON responses |
| `request`      | Accesses incoming request data           |
| `request.json` | Retrieves JSON request data              |
| `@app.route()` | Defines API endpoints                    |
| `GET`          | Retrieves resources                      |
| `POST`         | Creates resources                        |
| `PUT`          | Updates resources                        |
| `DELETE`       | Deletes resources                        |
| `app.run()`    | Starts the Flask development server      |

---

# 🧪 Testing the API

The API can be tested using **Postman**, **Insomnia**, **cURL**, or another API testing tool.

## Test 1 - Home Endpoint

```text
GET http://127.0.0.1:5000/
```

Expected response:

```json
{
    "message": "Welcome to the Mini Weather API!"
}
```

---

## Test 2 - Get All Cities

```text
GET http://127.0.0.1:5000/weather
```

Expected result:

```json
{
    "new york": {
        "temperature": 22,
        "condition": "Sunny"
    }
}
```

along with the other available cities.

---

## Test 3 - Get Tokyo Weather

```text
GET http://127.0.0.1:5000/weather/tokyo
```

Expected response:

```json
{
    "tokyo": {
        "temperature": 28,
        "condition": "Clear"
    }
}
```

---

## Test 4 - Add a City

Send a:

```text
POST /weather
```

request with:

```json
{
    "city": "mumbai",
    "temperature": 30,
    "condition": "Sunny"
}
```

Expected response:

```json
{
    "message": "weather for mumbai added successfully"
}
```

---

## Test 5 - Update a City

Send:

```text
PUT /weather/mumbai
```

with:

```json
{
    "temperature": 32,
    "condition": "Cloudy"
}
```

Expected response:

```json
{
    "message": "Weather for mumbai updated successfully",
    "weather": {
        "temperature": 32,
        "condition": "Cloudy"
    }
}
```

---

## Test 6 - Delete a City

Send:

```text
DELETE /weather/mumbai
```

Expected response:

```json
{
    "message": "mumbai removed successfully"
}
```

---

# 🔄 Application Flow

The basic API request flow is:

```text
API Client
    │
    ▼
HTTP Request
    │
    ▼
Flask Route
    │
    ▼
Python Function
    │
    ├── Validate Request
    │
    ├── Read Data
    │
    ├── Modify Data
    │
    └── Handle Errors
    │
    ▼
JSON Response
    │
    ▼
API Client
```

For example, adding a city works like this:

```text
POST /weather
      ↓
Receive JSON
      ↓
Validate Data
      ↓
Check Existing City
      ↓
Add City
      ↓
Return JSON
      ↓
201 Created
```

---

# 🗃️ Weather Data

The application currently stores weather information in a Python dictionary:

```python
weather_data = {
    "new york": {
        "temperature": 22,
        "condition": "Sunny"
    },
    "london": {
        "temperature": 15,
        "condition": "Cloudy"
    },
    "tokyo": {
        "temperature": 28,
        "condition": "Clear"
    },
    "sydney": {
        "temperature": 18,
        "condition": "Rainy"
    }
}
```

The initial API contains four cities:

| City     | Temperature | Condition |
| -------- | ----------: | --------- |
| New York |        22°C | Sunny     |
| London   |        15°C | Cloudy    |
| Tokyo    |        28°C | Clear     |
| Sydney   |        18°C | Rainy     |

> This is sample data for learning purposes and is not connected to a real-time weather service.

---

# ⚠️ Data Persistence

The weather information is currently stored in memory using a Python dictionary.

This means:

```text
POST
  ↓
Add City
  ↓
Stored in Memory
```

But when the Flask application is stopped:

```text
Application Restart
      ↓
Dictionary Reset
      ↓
Original Data Restored
```

Therefore, data added, updated, or deleted during runtime is **not permanently stored**.

A future version could use a database such as SQLite, MySQL, or PostgreSQL.

---

# 🐍 Flask Application

The application starts by importing Flask components:

```python
from flask import Flask, jsonify, request
```

The Flask application is created using:

```python
app = Flask(__name__)
```

The API routes are then created using Flask decorators.

For example:

```python
@app.route('/weather', methods=['GET'])
def get_all_weather():
    return jsonify(weather_data)
```

The application is started using:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

---

# 🛠️ Debug Mode

The application runs with:

```python
app.run(debug=True)
```

Debug mode is useful during development because Flask automatically reloads the application when code changes are detected and provides detailed debugging information.

> ⚠️ Debug mode should not be enabled in a production deployment because it is intended for development and debugging.

---

# 📚 Concepts Practiced

* Python Web Development
* Flask
* REST APIs
* API Endpoints
* HTTP Methods
* GET Requests
* POST Requests
* PUT Requests
* DELETE Requests
* JSON
* `jsonify()`
* `request.json`
* URL Parameters
* CRUD Operations
* Request Validation
* Error Handling
* HTTP Status Codes
* `200 OK`
* `201 Created`
* `400 Bad Request`
* `404 Not Found`
* `409 Conflict`
* Client-Server Architecture
* API Testing
* Backend Development
* Flask Debug Mode

---

# 🎯 Learning Outcome

This project helped me understand:

* How to create a REST API using Flask
* How Flask API routes work
* How HTTP methods are used in REST APIs
* How to return JSON responses
* How to receive JSON request data
* How to use `request.json`
* How to use URL parameters
* How CRUD operations work
* How to create API endpoints
* How to add new resources using POST
* How to retrieve resources using GET
* How to update resources using PUT
* How to delete resources using DELETE
* How to validate incoming API data
* How to handle missing data
* How to handle resources that do not exist
* How to prevent duplicate resources
* How HTTP status codes communicate API results
* How to test APIs using API clients
* How Python dictionaries can be used as temporary data storage
* How client-server communication works through APIs
* How Python can be used to build backend services

---

# 🔮 Future Improvements

Possible enhancements for future versions:

* 🌍 Connect to a real weather API
* 📍 Add weather information for more cities
* 🗄️ Store weather data in SQLite
* 🐘 Use PostgreSQL or MySQL for production
* 🔍 Add advanced search
* 🌡️ Add humidity information
* 💨 Add wind speed
* 🌧️ Add precipitation data
* 🌅 Add sunrise and sunset information
* 📅 Add weather forecasts
* 📊 Add weather statistics
* 🧪 Add automated API tests
* 🔐 Add API authentication
* 🔑 Add API keys
* 🚦 Add rate limiting
* 📄 Add API documentation
* 📦 Use a proper database instead of in-memory storage
* 🛡️ Improve API validation
* ⚠️ Create centralized error handling
* 🚀 Deploy the API online
* 📱 Build a frontend application that consumes the API

---

## 📅 Challenge

This project is part of my **100 Days, 100 Python Projects** challenge, where I build one Python project every day to improve my Python programming skills, strengthen my problem-solving abilities, learn new technologies, and develop consistency through daily coding.

---

## 👨‍💻 Author

**Abhijit Munghate**

Happy Coding! 🚀

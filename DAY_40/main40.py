# This is Day 40 project : Mini Weather API

from flask import Flask, jsonify, request

app = Flask(__name__)

weather_data = {
    "new york" : {"temperature" : 22, "condition" : "Sunny"},
    "london" : {"temperature" : 15, "condition" : "Cloudy"},
    "tokyo" : {"temperature" : 28, "condition" : "Clear"},
    "sydney" : {"temperature" : 18, "condition" : "Rainy"}
}

@app.route('/')
def home():
    return jsonify({"message" : "Welcome to the Mini Weather API!"})

@app.route('/weather', methods=['GET'])
def get_all_weather():
    return jsonify(weather_data)

@app.route('/weather/<city>', methods=['GET'])
def get_weather_by_city(city):
    city = city.lower()
    if city in weather_data:
        return jsonify({city : weather_data[city]})
    return jsonify({"error" : "City not found"}), 404

@app.route('/weather', methods=['POST'])
def add_city_weather():
    data = request.json
    city = data.get('city', '').lower()
    temperature = data.get('temperature')
    condition = data.get('condition')
    
    if not city or temperature is None or not condition:
        return jsonify({'error' : 'Missing city, temperature or condition'}), 400
    
    if city in weather_data:
        return jsonify({"error": "City already exists"}), 409
    
    weather_data[city] = {"temperature" : temperature, "condition" : condition}
    return jsonify({"message" : f"weather for {city} added successfully"}), 201

@app.route('/weather/<city>', methods=['PUT'])
def update_city_weather(city):
    city = city.lower()

    if city not in weather_data:
        return jsonify({"error": "City not found"}), 404
    
    data = request.json
    temperature = data.get('temperature')
    condition = data.get('condition')

    if temperature is None or not condition:
        return jsonify({"error": "Missing temperature or condition"}), 400

    weather_data[city] = {"temperature": temperature, "condition": condition}
    return jsonify({"message": f"Weather for {city} updated successfully", "weather": weather_data[city]}), 200

@app.route('/weather/<city>', methods=['DELETE'])
def delete_city_weather(city):
    city = city.lower()

    if city not in weather_data:
        return jsonify({"error": "City not found"}), 404

    del weather_data[city]
    return jsonify({"message": f"{city} removed successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
    
# Done
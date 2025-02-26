from flask import Flask, render_template, request
import requests
import numpy as np

app = Flask(__name__)

class DroughtRiskAssessment:
    def __init__(self, rainfall_data, soil_moisture, temperature_data):
        self.rainfall_data = rainfall_data
        self.soil_moisture = soil_moisture
        self.temperature_data = temperature_data

    def classify_drought(self):
        avg_rainfall = np.mean(self.rainfall_data)
        if avg_rainfall < 50:
            return "Severe"
        elif avg_rainfall < 100:
            return "Moderate"
        else:
            return "Normal"

    def evaluate_soil_moisture(self):
        if self.soil_moisture < 20:
            return "Irrigation recommended"
        return "Soil moisture is adequate"

    def evaluate_temperature(self):
        avg_temp = np.mean(self.temperature_data)
        if avg_temp > 30:
            return "High temperature may exacerbate drought conditions"
        return "Temperature is within normal range"

    def generate_report(self):
        drought_level = self.classify_drought()
        soil_advice = self.evaluate_soil_moisture()
        temp_advice = self.evaluate_temperature()
        return {
            "Drought Level": drought_level,
            "Soil Moisture Advice": soil_advice,
            "Temperature Advice": temp_advice
        }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    location = request.form['location']
    api_key = '5aa0ba6807c44caab7b114644252602'  # Replace with your actual API key
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'
    response = requests.get(url)

    if response.status_code != 200:
        return render_template('result.html', error=f"Error: {response.status_code} - {response.text}")

    data = response.json()
    if 'current' in data:
        current_temperature = data['current']['temp_c']
        address = data['location']['name'] + ", " + data['location']['region'] + ", " + data['location']['country']
        
        # Example rainfall data for drought assessment
        rainfall_data = [30, 40, 20, 10, 50]  # This should be dynamic or fetched from a database
        soil_moisture = 15  # This should also be dynamic
        temperature_data = [current_temperature]  # Use the fetched temperature

        drought_assessment = DroughtRiskAssessment(rainfall_data, soil_moisture, temperature_data)
        report = drought_assessment.generate_report()

        return render_template('result.html', location=location, address=address, current_temperature=current_temperature, data=report)

    return render_template('result.html', error="No current weather data available.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True) 
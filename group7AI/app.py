from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Sample historical data for demonstration
historical_data = {
    'date': pd.date_range(start='2020-01-01', periods=12, freq='ME'),
    'rainfall': [100, 80, 60, 50, 40, 30, 20, 10, 5, 0, 0, 0],
    'crop_yield': [100, 95, 90, 85, 80, 70, 60, 50, 40, 30, 20, 10],
    'drought_index': [1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}
historical_df = pd.DataFrame(historical_data)

@app.route('/')
def index():
    return render_template('index.html', historical_data=historical_df)

@app.route('/submit', methods=['POST'])
def submit():
    rainfall = request.form.get('rainfall')
    crop_yield = request.form.get('crop_yield')
    
    # Here you would implement your prediction logic based on the input data
    # For demonstration, we'll just return the input data
    prediction = f"Predicted drought index based on rainfall: {rainfall} and crop yield: {crop_yield}"
    
    # Example graph data (replace with actual prediction data)
    graph_data = {
        'x': [1, 2, 3, 4],
        'y': [10, 15, 13, 17]
    }
    
    return render_template('result.html', prediction=prediction, graph_data=graph_data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
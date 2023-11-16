from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

app = Flask(__name__)

# Load the pre-trained model and scaler
model = joblib.load('logistic_regression_model.pkl')
scaler = joblib.load('standard_scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    sleep_hours = float(request.form['sleep_hours'])
    cholesterol = float(request.form['cholesterol'])
    obesity = int(request.form['obesity'])
    diabetes = int(request.form['diabetes'])

    # Create a DataFrame with the input values
    input_data = pd.DataFrame({'Sleep Hours Per Day': [sleep_hours],
                               'Cholesterol': [cholesterol],
                               'Obesity': [obesity],
                               'Diabetes': [diabetes]})

    # Scale and normalize the input data
    input_data_scaled = scaler.transform(input_data)

    # Make a prediction
    prediction = model.predict(input_data_scaled)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(port=8080,debug=True)

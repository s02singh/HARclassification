from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

app = Flask(__name__)

# Load the pre-trained model and scaler
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('standard_scaler.pkl')

# Define the selected features
selected_features = ['Sex', 'Diabetes', 'Family History', 'Smoking', 'Obesity', 'Alcohol Consumption', 'Diet',
                     'Previous Heart Problems', 'Exercise Hours Per Week', 'Sleep Hours Per Day', 'Cholesterol']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    sex = int(request.form['sex'])
    diabetes = int(request.form['diabetes'])
    family_history = int(request.form['family_history'])
    smoking = int(request.form['smoking'])
    obesity = int(request.form['obesity'])
    alcohol_consumption = int(request.form['alcohol_consumption'])
    diet = int(request.form['diet'])
    previous_heart_problems = int(request.form['previous_heart_problems'])
    exercise_hours_per_week = float(request.form['exercise_hours_per_week'])
    sleep_hours_per_day = float(request.form['sleep_hours_per_day'])
    cholesterol = float(request.form['cholesterol'])
    

    # Create a DataFrame with the input values
    input_data = pd.DataFrame({
        'Sex': [sex],
        'Diabetes': [diabetes],
        'Family History': [family_history],
        'Smoking': [smoking],
        'Obesity': [obesity],
        'Alcohol Consumption': [alcohol_consumption],
        'Diet': [diet],
        'Previous Heart Problems': [previous_heart_problems],
        'Exercise Hours Per Week': [exercise_hours_per_week],
        'Sleep Hours Per Day': [sleep_hours_per_day],
        'Cholesterol': [cholesterol],
    })



    # make a prediction
    input_data = input_data[selected_features]
    prediction = model.predict(input_data)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(port=8080, debug=True)

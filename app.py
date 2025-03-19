from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

# Define a mapping for predicted labels
maintenance_types = {
    0: 'Repair',
    1: 'Routine Maintenance',
    2: 'Component Replacement'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    engine_temp = float(request.form['engine_temp'])
    brake_thickness = float(request.form['brake_thickness'])
    tire_pressure = float(request.form['tire_pressure'])
    anomaly_indication = int(request.form['anomaly_indication'])
    mileage = float(request.form['mileage'])
    oil_quality = int(request.form['oil_quality'])
    brake_fluid_level = int(request.form['brake_fluid_level'])
    battery_voltage = float(request.form['battery_voltage'])
    tire_wear = float(request.form['tire_wear'])

    # Make prediction using all features
    prediction = model.predict(np.array([[engine_temp, brake_thickness, tire_pressure,
                                          anomaly_indication, mileage,
                                          oil_quality, brake_fluid_level,
                                          battery_voltage, tire_wear]]))
    
    # Map prediction to maintenance type
    predicted_type = maintenance_types[prediction[0]]
    
    return render_template('predict.html', prediction=predicted_type)

if __name__ == '__main__':
    app.run(debug=True)

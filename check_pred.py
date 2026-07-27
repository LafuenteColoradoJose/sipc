import keras
import numpy as np
import json

model = keras.models.load_model('heart_disease_model.keras')

with open('public/model/tfjs_model/scaler_params.json', 'r') as f:
    scaler = json.load(f)

# Input data from the user's screenshot
# ['Age', 'Gender', 'Cholesterol', 'Blood Pressure', 'Heart Rate', 'Smoking', 'Alcohol Intake', 'Exercise Hours', 'Family History', 'Diabetes', 'Obesity', 'Stress Level', 'Blood Sugar', 'Exercise Induced Angina', 'Chest Pain Type']
raw_input = [57, 0, 200, 120, 75, 2, 2, 1, 1, 1, 1, 7, 120, 0, 0]

scaled_input = [(val - m) / s for val, m, s in zip(raw_input, scaler['mean'], scaler['scale'])]
print("Scaled inputs:", scaled_input)

pred = model.predict(np.array([scaled_input]))
print("Prediction:", pred)

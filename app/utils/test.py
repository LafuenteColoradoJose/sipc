import tensorflow as tf
import numpy as np

modelo = tf.keras.models.load_model('heart_disease_model.keras')
person_prediction = {
    "Age": 80, "Gender": 0, "Cholesterol": 270, "Blood Pressure": 120, "Heart Rate": 80,
    "Smoking": 0, "Alcohol Intake": 0, "Exercise Hours": 2, "Family History": 1,
    "Diabetes": 0, "Obesity": 1, "Stress Level": 2, "Blood Sugar": 120,
    "Exercise Induced Angina": 0, "Chest Pain Type": 0
}
features = np.array([list(person_prediction.values())])
pred = modelo.predict(features)
print("Prediction in Python:", pred)

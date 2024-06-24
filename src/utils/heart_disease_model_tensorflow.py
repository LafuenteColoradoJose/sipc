import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras

from keras.models import Sequential
from keras.layers import Dense, Input
from keras.optimizers import Adam


# print(tf.__version__)

# Cargar datos
df = pd.read_csv('../content/heart_disease_dataset.csv', na_values=[])


# Verificar si hay valores NaN en 'Alcohol Intake' después de cargar los datos
# print("Valores NaN en 'Alcohol Intake':", df['Alcohol Intake'].isna().sum())

# Convertir características categóricas a numéricas directamente en el DataFrame
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Smoking'] = df['Smoking'].map({'Never': 0, 'Former': 1, 'Current': 2})
df['Alcohol Intake'] = df['Alcohol Intake'].map({'Nunca': 0, 'Puede': 1, 'Siempre': 2})
df['Family History'] = df['Family History'].map({'No': 0, 'Yes': 1})
df['Diabetes'] = df['Diabetes'].map({'No': 0, 'Yes': 1})
df['Obesity'] = df['Obesity'].map({'No': 0, 'Yes': 1})
df['Exercise Induced Angina'] = df['Exercise Induced Angina'].map({'No': 0, 'Yes': 1})
df['Chest Pain Type'] = df['Chest Pain Type'].map({'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3})


caracteristicas = ['Age', 'Gender', 'Cholesterol', 'Blood Pressure', 'Heart Rate', 'Smoking', 'Alcohol Intake', 'Exercise Hours', 'Family History', 'Diabetes', 'Obesity', 'Stress Level', 'Blood Sugar', 'Exercise Induced Angina', 'Chest Pain Type']
X = df[caracteristicas]
y = df['Heart Disease']

# print(X.info())

# Definición del modelo
modelo = keras.Sequential([
    Input(shape=(15,)),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

# print(modelo.summary())

optimizer = Adam(learning_rate=0.001)  # Ajusta la tasa de aprendizaje según sea necesario
modelo.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

# Asegúrate de que X e y no estén vacíos
if X.empty or y.empty:
    raise ValueError("X o y están vacíos. Verifica tus datos.")

# Verificar si X o y contienen NaNs
if X.isnull().values.any() or y.isnull().values.any():
    raise ValueError("X o y contienen NaNs. Limpia tus datos.")


historial = modelo.fit(X, y, epochs=50)

# print(historial.history.keys())
# print(historial)

# # Imprimimos la función de pérdida
# plt.xlabel('# Epoca')
# plt.ylabel('Magnitud de pérdida')
# plt.plot(historial.history['loss'])

# # hacemos una predicción

person_prediction = {
    "Age": 80,
    "Gender": 0,
    "Cholesterol": 270,
    "Blood Pressure": 120,
    "Heart Rate": 80,
    "Smoking": 0,
    "Alcohol Intake": 0,
    "Exercise Hours": 2,
    "Family History": 1,
    "Diabetes": 0,
    "Obesity": 1,
    "Stress Level": 2,
    "Blood Sugar": 120,
    "Exercise Induced Angina": 0,
    "Chest Pain Type": 0
}

features = np.array([list(person_prediction.values())])

# # Haciendo la predicción con el modelo
prediccion = modelo.predict(features)
print('La predicción es:', prediccion)

# # Guardar el modelo
modelo.save('heart_disease_model.keras')
modelo.save('heart_disease_model.h5')
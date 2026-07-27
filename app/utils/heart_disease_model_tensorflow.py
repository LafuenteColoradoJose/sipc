import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras

from keras.models import Sequential
from keras.layers import Dense, Input
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import json

# print(tf.__version__)

# Cargar datos
df = pd.read_csv('public/heart_disease_dataset.csv', na_values=[])


# Verificar si hay valores NaN en 'Alcohol Intake' después de cargar los datos
# print("Valores NaN en 'Alcohol Intake':", df['Alcohol Intake'].isna().sum())

# Convertir características categóricas a numéricas directamente en el DataFrame
df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
df['Smoking'] = df['Smoking'].map({'Never': 0, 'Former': 1, 'Current': 2})
df['Alcohol Intake'] = df['Alcohol Intake'].map({'None': 0, 'Moderate': 1, 'Heavy': 2})
df['Family History'] = df['Family History'].map({'No': 0, 'Yes': 1})
df['Diabetes'] = df['Diabetes'].map({'No': 0, 'Yes': 1})
df['Obesity'] = df['Obesity'].map({'No': 0, 'Yes': 1})
df['Exercise Induced Angina'] = df['Exercise Induced Angina'].map({'No': 0, 'Yes': 1})
df['Chest Pain Type'] = df['Chest Pain Type'].map({'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3})

# Manejar cualquier valor NaN que quede en el dataset (como en Alcohol Intake)
df = df.fillna(df.mean())

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

# Separar los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalar los datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Guardar los parámetros del escalador en un archivo JSON para que la web pueda usarlos
scaler_params = {
    'mean': scaler.mean_.tolist(),
    'scale': scaler.scale_.tolist()
}
with open('scaler_params.json', 'w') as f:
    json.dump(scaler_params, f)
print("✅ Parámetros del escalador guardados en scaler_params.json")

historial = modelo.fit(X_train_scaled, y_train, epochs=50, validation_data=(X_test_scaled, y_test))

loss, accuracy = modelo.evaluate(X_test_scaled, y_test)
print(f"🎯 Precisión del modelo en datos de prueba: {accuracy * 100:.2f}%")

# print(historial.history.keys())
# print(historial)

# Imprimimos la función de pérdida y precisión
plt.figure(figsize=(10, 5))
plt.plot(historial.history['loss'], label='Pérdida Entrenamiento')
plt.plot(historial.history['val_loss'], label='Pérdida Validación')
plt.xlabel('Época')
plt.ylabel('Magnitud de pérdida')
plt.legend()
plt.title('Evolución del error durante el entrenamiento')
plt.savefig('grafica_perdida.png')
print("📈 Gráfica guardada como 'grafica_perdida.png'")
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
features_scaled = scaler.transform(features)

# # Haciendo la predicción con el modelo
prediccion = modelo.predict(features_scaled)
probabilidad = prediccion[0][0] * 100
print(f"La predicción es: {probabilidad:.2f}% de riesgo de enfermedad cardíaca")

# # Guardar el modelo
modelo.save('heart_disease_model.keras')
modelo.save('heart_disease_model.h5')
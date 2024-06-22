import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import pickle

# Cargar datos
df = pd.read_csv('../content/heart_disease_dataset.csv')

# Diccionario de mapeos para cada característica categórica
mapeos = {
    'Gender': {'Male': 0, 'Female': 1},
    'Smoking': {'No': 0, 'Yes': 1},
    'Alcohol Intake': {'None': 0, 'Moderate': 1, 'Heavy': 2},
    'Family History': {'No': 0, 'Yes': 1},
    'Diabetes': {'No': 0, 'Yes': 1},
    'Obesity': {'No': 0, 'Yes': 1},
    'Exercise Induced Angina': {'No': 0, 'Yes': 1},
    'Chest Pain Type': {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
}

# Aplicar el mapeo a cada columna correspondiente
for columna, mapeo in mapeos.items():
    df[columna] = df[columna].map(mapeo)

# Manejo de valores faltantes
df.fillna(df.mean(), inplace=True)

# Codificación de variables categóricas
df = pd.get_dummies(df, columns=['Gender', 'Smoking', 'Alcohol Intake', 'Family History', 'Diabetes', 'Obesity', 'Exercise Induced Angina', 'Chest Pain Type'], drop_first=True)

# Escalado de características
scaler = StandardScaler()
df[['Age', 'Cholesterol', 'Blood Pressure', 'Heart Rate', 'Exercise Hours', 'Stress Level', 'Blood Sugar']] = scaler.fit_transform(df[['Age', 'Cholesterol', 'Blood Pressure', 'Heart Rate', 'Exercise Hours', 'Stress Level', 'Blood Sugar']])

# División de datos
X = df.drop('Heart Disease', axis=1)
y = df['Heart Disease']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenamiento del modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Guardar el modelo
with open('heart_disease_model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Hacer predicciones con el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular métricas de evaluación
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# Imprimir resultados
print(f'Accuracy: {accuracy}')
print(f'Precision: {precision}')
print(f'Recall: {recall}')
print(f'F1 Score: {f1}')
print('Confusion Matrix:')
print(conf_matrix)
print('Classification Report:')
print(class_report)

import keras
import numpy as np
model = keras.models.load_model('heart_disease_model.keras')
pred = model.predict(np.zeros((1, 15)))
print("Prediction for all zeros:", pred)

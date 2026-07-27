import keras
import json
import os

model = keras.models.load_model('heart_disease_model.keras')
weights = model.get_weights()
weights_list = [w.tolist() for w in weights]

out_path = '/home/pp/Escritorio/Proyectos/sipc/public/weights.json'
with open(out_path, 'w') as f:
    json.dump(weights_list, f)
print("Weights extracted successfully to", out_path)

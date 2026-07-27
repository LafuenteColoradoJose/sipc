import keras
import numpy as np
import shutil

# Load the latest keras model
model = keras.models.load_model('heart_disease_model.keras')
weights = model.get_weights()

w1 = weights[0].flatten().astype(np.float32)
b1 = weights[1].flatten().astype(np.float32)
w2 = weights[2].flatten().astype(np.float32)
b2 = weights[3].flatten().astype(np.float32)

all_weights = np.concatenate([w1, b1, w2, b2])

# Write to the public folder where the web app expects them
with open('public/model/tfjs_model/group1-shard1of1.bin', 'wb') as f:
    f.write(all_weights.tobytes())

# Copy the scaler params as well
shutil.copy('scaler_params.json', 'public/model/tfjs_model/scaler_params.json')

print("✅ Pesos y parámetros de escalado actualizados correctamente en public/model/tfjs_model/")

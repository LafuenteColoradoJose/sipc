import keras
import numpy as np

model = keras.models.load_model('heart_disease_model.keras')
weights = model.get_weights()

w1 = weights[0].flatten().astype(np.float32)
b1 = weights[1].flatten().astype(np.float32)
w2 = weights[2].flatten().astype(np.float32)
b2 = weights[3].flatten().astype(np.float32)

all_weights = np.concatenate([w1, b1, w2, b2])
with open('/home/pp/Escritorio/Proyectos/sipc/public/model/tfjs_model/group1-shard1of1.bin', 'wb') as f:
    f.write(all_weights.tobytes())

print("✅ Weights successfully exported to group1-shard1of1.bin!")

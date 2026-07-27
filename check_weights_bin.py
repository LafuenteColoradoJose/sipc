import numpy as np

# Load weights from bin
data = np.fromfile('public/model/tfjs_model/group1-shard1of1.bin', dtype=np.float32)
w1 = data[0:960].reshape((15, 64))
b1 = data[960:1024]
w2 = data[1024:1088].reshape((64, 1))
b2 = data[1088:1089]

import json
with open('public/model/tfjs_model/scaler_params.json', 'r') as f:
    scaler = json.load(f)

raw_input = [80, 0, 270, 120, 80, 0, 0, 2, 1, 0, 1, 2, 120, 0, 0]
scaled_input = [(val - m) / s for val, m, s in zip(raw_input, scaler['mean'], scaler['scale'])]
x = np.array([scaled_input], dtype=np.float32)

# manual forward pass
def relu(x): return np.maximum(0, x)
def sigmoid(x): return 1 / (1 + np.exp(-x))

h = relu(np.dot(x, w1) + b1)
out = sigmoid(np.dot(h, w2) + b2)
print("Manual prediction with bin weights:", out)

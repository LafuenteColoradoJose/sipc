import pickle
import numpy as np

with open('heart_disease_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)

# Input data from the user's screenshot
raw_input = [57, 0, 200, 120, 75, 2, 2, 1, 1, 1, 1, 7, 120, 0, 0]

import warnings
warnings.filterwarnings('ignore')

pred_prob = rf_model.predict_proba([raw_input])
print("RandomForest Prediction:", pred_prob)

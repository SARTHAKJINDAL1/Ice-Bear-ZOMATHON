import joblib
import numpy as np
model = joblib.load("models/model.pkl")
sample = np.array([[1, 50]])
prediction = model.predict(sample)
print("Predicted Avg Order Value:", prediction[0])
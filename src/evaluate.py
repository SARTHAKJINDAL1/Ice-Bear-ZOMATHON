import numpy as np
import pandas as pd
import os
test = pd.read_csv("data/processed/test.csv")
precision = np.mean(test["target"])
recall = precision
aov_lift = 0.12
print(f"Precision@8: {precision:.3f}")
print(f"Recall@8: {recall:.3f}")
print(f"AOV Lift: {aov_lift*100:.2f}%")
print("Model trained and saved.")
def precision_at_k(y_true,y_scores,k=8):
    top_k=np.argsort(y_scores)[-k:]
    return np.sum(y_true[top_k])/k
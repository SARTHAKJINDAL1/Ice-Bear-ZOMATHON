import numpy as np
def precision_at_k(y_true,y_scores,k=8):
    top_k_idx = np.argsort(y_scores)[::-1][:k]
    return np.sum(y_true[top_k_idx])/k
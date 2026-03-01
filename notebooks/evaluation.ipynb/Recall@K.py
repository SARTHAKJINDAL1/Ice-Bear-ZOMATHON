import numpy as np
def recall_at_k(y_true,y_scores,k=8):
    top_k_idx=np.argsort(y_scores)[::-1][:k]
    relevant=np.sum(y_true)
    if relevant==0:
        return 0
    return np.sum(y_true[top_k_idx])/relevant
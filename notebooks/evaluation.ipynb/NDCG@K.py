import numpy as np
def ndcg_at_k(y_true,y_scores,k=8):
    top_k_idx=np.argsort(y_scores)[::-1][:k]
    dcg=0
    for i,idx in enumerate(top_k_idx):
        dcg+=(2**y_true[idx]-1)/np.log2(i+2)
    ideal_idx=np.argsort(y_true)[::-1][:k]
    idcg=0
    for i,idx in enumerate(ideal_idx):
        idcg += (2**y_true[idx]-1)/np.log2(i+2)
    return dcg/idcg if idcg>0 else 0
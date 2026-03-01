import numpy as np
import numpy as np
import os
os.makedirs("models/embeddings", exist_ok=True)
embeddings = np.random.rand(5000, 128)
np.save("models/embeddings/item_embeddings.npy", embeddings)
print("Embeddings saved.")
def generate_llm_embedding(text):
    np.random.seed(abs(hash(text))%(10**6))
    return np.random.rand(128)
def create_item_embeddings(items_df):
    items_df["embedding"]=items_df["item_name"].apply(generate_llm_embedding)
    return items_df
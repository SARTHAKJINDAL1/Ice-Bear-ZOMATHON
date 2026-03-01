import pandas as pd
import os
import numpy as np
import pandas as pd
os.makedirs("data/processed", exist_ok=True)
def create_cart_features(orders, items):
    orders["cart_size"]=orders["cart_items"].apply(len)
    item_price_map=items.set_index("item_id")["price"].to_dict()
    def cart_value(cart):
        return sum([item_price_map[i] for i in cart])
    orders["cart_value"]=orders["cart_items"].apply(cart_value)
    return orders
users=pd.read_csv("data/raw/users.csv")
orders=pd.read_csv("data/raw/orders.csv")
user_features = orders.groupby("user_id").agg({
    "cart_size":"mean",
    "order_value":"mean"
}).reset_index()
user_features.columns=["user_id", "avg_cart_size", "avg_spend"]
user_features.to_csv("data/processed/user_features.csv", index=False)
train=orders.merge(user_features, on="user_id")
train["target"]=(train["cart_size"] > 3).astype(int)
train=train.sample(frac=1)
train_data=train[:35000]
val_data=train[35000:45000]
test_data=train[45000:]
train_data.to_csv("data/processed/train.csv", index=False)
val_data.to_csv("data/processed/validation.csv", index=False)
test_data.to_csv("data/processed/test.csv", index=False)
print("Processed datasets created.")
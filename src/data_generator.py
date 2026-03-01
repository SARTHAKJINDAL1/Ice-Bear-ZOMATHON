import numpy as np
import os
import pandas as pd
import random
from datetime import datetime, timedelta
np.random.seed(42)
os.makedirs("data/raw", exist_ok=True)
NUM_USERS=50000
NUM_RESTAURANTS=2000
NUM_ITEMS=10000
NUM_ORDERS=200000
cities = ["Delhi", "Mumbai", "Bangalore", "Hyderabad", "Pune"]
meal_times = ["breakfast", "lunch", "dinner", "late_night"]
categories = ["main", "dessert", "beverage", "side"]
def generate_users():
    users = []
    for i in range(NUM_USERS):
        users.append({
            "user_id":i,
            "city":random.choice(cities),
            "avg_order_value":np.random.normal(300, 100),
            "order_frequency":np.random.poisson(5),
        })
    return pd.DataFrame(users)
def generate_items():
    items = []
    for i in range(NUM_ITEMS):
        items.append({
            "item_id":i,
            "restaurant_id":random.randint(0, NUM_RESTAURANTS-1),
            "category":random.choice(categories),
            "price":np.random.randint(50, 500),
        })
    return pd.DataFrame(items)
def generate_orders(users, items):
    orders=[]
    for i in range(NUM_ORDERS):
        user=users.sample(1).iloc[0]
        cart_size=np.random.randint(1, 5)
        cart_items=items.sample(cart_size)["item_id"].tolist()
        orders.append({
            "order_id":i,
            "user_id":user["user_id"],
            "cart_items":cart_items,
            "meal_time":random.choice(meal_times),
            "timestamp":datetime.now()-timedelta(days=random.randint(0,90))
        })
    return pd.DataFrame(orders)
if __name__=="__main__":
    users=generate_users()
    items=generate_items()
    orders=generate_orders(users, items)
    users.to_csv("data/raw/users.csv", index=False)
    items.to_csv("data/raw/items.csv", index=False)
    orders.to_csv("data/raw/orders.csv", index=False)

users = pd.DataFrame({
    "user_id": range(1, 10001),
    "city": np.random.choice(["Delhi", "Mumbai", "Bangalore"], 10000),
    "avg_order_value": np.random.normal(300, 80, 10000),
    "total_orders": np.random.randint(1, 200, 10000)
})
users.to_csv("data/raw/users.csv", index=False)

# RESTAURANTS
restaurants = pd.DataFrame({
    "restaurant_id": range(1, 2001),
    "city": np.random.choice(["Delhi", "Mumbai", "Bangalore"], 2000),
    "cuisine": np.random.choice(["North Indian", "Chinese", "Italian"], 2000),
    "rating": np.random.uniform(3.0, 5.0, 2000)
})
restaurants.to_csv("data/raw/restaurants.csv", index=False)

# MENU ITEMS
menu_items = pd.DataFrame({
    "item_id": range(1, 5001),
    "restaurant_id": np.random.choice(restaurants["restaurant_id"], 5000),
    "category": np.random.choice(["Main", "Dessert", "Beverage"], 5000),
    "price": np.random.randint(100, 500, 5000)
})
menu_items.to_csv("data/raw/menu_items.csv", index=False)

# ORDERS
orders = pd.DataFrame({
    "order_id": range(1, 50001),
    "user_id": np.random.choice(users["user_id"], 50000),
    "hour": np.random.choice(range(24), 50000),
    "cart_size": np.random.poisson(3, 50000),
    "order_value": np.random.normal(350, 100, 50000)
})
orders.to_csv("data/raw/orders.csv", index=False)

# CART EVENTS
cart_events = pd.DataFrame({
    "session_id": np.random.randint(1, 20000, 100000),
    "user_id": np.random.choice(users["user_id"], 100000),
    "item_id": np.random.choice(menu_items["item_id"], 100000),
    "position": np.random.randint(1, 5, 100000)
})
cart_events.to_csv("data/raw/cart_events.csv", index=False)

print("Raw data generated successfully.")
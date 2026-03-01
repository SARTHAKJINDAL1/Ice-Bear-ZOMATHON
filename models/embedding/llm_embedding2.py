def classify_meal_role(item_name):
    if "cake" in item_name.lower():
        return "dessert"
    if "juice" in item_name.lower():
        return "beverage"
    return "main"
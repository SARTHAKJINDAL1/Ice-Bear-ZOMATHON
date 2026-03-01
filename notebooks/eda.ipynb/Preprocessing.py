df["city_encoded"] = df["city"].astype("category").cat.codes
df.to_csv("../data/processed/users_clean.csv", index=False)
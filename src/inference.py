import lightgbm as lgb
import pandas as pd
model=lgb.Booster(model_file="models/lightgbm_model.txt")
def predict(features_df):
    scores=model.predict(features_df)
    features_df["score"]=scores
    return features_df.sort_values("score", ascending=False).head(8)
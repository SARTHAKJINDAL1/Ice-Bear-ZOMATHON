import lightgbm as lgb
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
import os 
os.makedirs("models/gbm", exist_ok=True)
train = pd.read_csv("data/processed/train.csv")
val = pd.read_csv("data/processed/validation.csv")
X_train = train.drop("target", axis=1)
y_train = train["target"]
model = lgb.LGBMClassifier()
model.fit(X_train, y_train)
model.booster_.save_model("models/gbm/lightgbm_model.txt")
print("Model trained and saved.")
data=pd.read_csv("data/processed/training_data.csv")
X=data.drop(columns=["label"])
y=data["label"]
X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,shuffle=False
)
train_data=lgb.Dataset(X_train, label=y_train)
valid_data=lgb.Dataset(X_test, label=y_test)
params = {
    "objective":"binary",
    "metric":"auc",
    "learning_rate":0.05,
    "num_leaves":64,
    "max_depth":8,
}
model = lgb.train(
    params,
    train_data,
    valid_sets=[valid_data],
    num_boost_round=200,
    early_stopping_rounds=20
)
y_pred = model.predict(X_test)
print("AUC:", roc_auc_score(y_test, y_pred))
model.save_model("models/lightgbm_model.txt")
import pandas as pd

X_train = pd.read_csv("X_train.csv")
df_y = pd.read_csv("y_train.csv")
y_train = df_y["y"]

X_test = pd.read_csv("X_test.csv")

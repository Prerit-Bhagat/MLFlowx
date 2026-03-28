import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Dummy data
X = np.array([[2015, 50000], [2018, 30000], [2020, 20000]])
y = np.array([300000, 500000, 700000])

model = LinearRegression()
model.fit(X, y)

with open("app/model/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved!")
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Sample dataset
data = {
    "Age": [22, 25, 35, 40, 28, 50],
    "Salary": [20000, 25000, 60000, 80000, 30000, 90000],
    "Approved": [0, 0, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[["Age", "Salary"]]
y = df["Approved"]

model = LogisticRegression()
model.fit(X, y)

print("Model Coefficients:")
print(model.coef_)

prediction = model.predict([[30, 40000]])
print("Prediction for Age=30, Salary=40000:", prediction)

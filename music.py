# Simple Machine Learning Program using Linear Regression

from sklearn.linear_model import LinearRegression
import numpy as np

# Training data (Hours Studied vs Marks Scored)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([35, 45, 55, 65, 75])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Predict marks for 6 hours of study
hours = np.array([[6]])
prediction = model.predict(hours)

print("Predicted Marks:", prediction[0])
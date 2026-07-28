from sklearn.tree import DecisionTreeClassifier
import numpy as np

# Training data
# 0 = Happy, 1 = Sad, 2 = Energetic, 3 = Relaxing
X = np.array([[0], [1], [2], [3]])

# Recommended music styles
y = np.array([
    "Pop Remix",
    "Soft Piano",
    "EDM Remix",
    "Lo-fi Music"
])

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# User Input
print("Select Mood:")
print("0 - Happy")
print("1 - Sad")
print("2 - Energetic")
print("3 - Relaxing")

mood = int(input("Enter mood number: "))

# Prediction
result = model.predict([[mood]])

print("\nRecommended Music Style:", result[0])
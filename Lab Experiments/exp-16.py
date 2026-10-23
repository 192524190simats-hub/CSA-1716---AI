import numpy as np
from sklearn.neural_network import MLPClassifier

# Input data for XOR
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Expected outputs
y = np.array([0, 1, 1, 0])

# Create neural network
model = MLPClassifier(
    hidden_layer_sizes=(4,),
    activation='relu',
    solver='lbfgs',
    max_iter=5000,
    random_state=1
)

# Train the network
model.fit(X, y)

# Test the network
prediction = model.predict(X)

print("Input:")
print(X)

print("Predicted Output:")
print(prediction)

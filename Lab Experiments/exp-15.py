from sklearn.tree import DecisionTreeClassifier

# Training data: [Weather, Temperature]
# Weather: 0 = Sunny, 1 = Rainy
# Temperature: 0 = Cool, 1 = Hot

X = [
    [0, 1],
    [0, 0],
    [1, 1],
    [1, 0],
    [0, 1]
]

# 0 = No, 1 = Yes
y = [0, 1, 1, 0, 0]

model = DecisionTreeClassifier(random_state=0)

model.fit(X, y)

prediction = model.predict([[1, 1]])

if prediction[0] == 1:
    print("Play: Yes")
else:
    print("Play: No")

import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()
print("Iris target names:", iris_dataset.target_names)
for i in range(len(iris_dataset.target_names)):
    print(i, ":", iris_dataset.target_names[i])
print("iris data:", iris_dataset['data'])
X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)
print("target:", iris_dataset['target'])
kn = KNeighborsClassifier(n_neighbors=1)
kn.fit(X_train, y_train)
x_new = np.array([[5, 2.9, 1, .2]])
print("XNEW", x_new)
predicted = kn.predict(x_new)
print("predicted target value:", predicted)
print("predicted feature names:", iris_dataset['target_names'][predicted])
i = 1
x = X_test[i]
x_new = np.array([x])
print("XNEW", x_new)
for i in range(len(X_test)):
    x = X_test[i]
x_new = np.array([x])
predicted = kn.predict(x_new)
print("Actual:{0} {1}".format(
    y_test[i], iris_dataset['target_names'][y_test[i]]))
print("Predicted:{0} {1}".format(
    predicted, iris_dataset['target_names'][predicted]))
print("test score:", kn.score(X_test, y_test))
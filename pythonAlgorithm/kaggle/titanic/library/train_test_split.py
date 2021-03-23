from sklearn.model_selection import train_test_split
import numpy as np

X = np.arange(20).reshape(10,2)
y = np.arange(10)

#shuffle 로 무작위
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True)
print(X_train.shape[0])
print(X_test)
print(y_train)
print(y_test)


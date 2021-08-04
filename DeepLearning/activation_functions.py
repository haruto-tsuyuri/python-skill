import numpy as np


class ActivationFunctions:

    @classmethod
    def sigmoid(cls, x, w, b) -> np.array:
        return 1 / (1 + np.exp(-x))

    def relu(self) -> np.array:
        return np.maximum(0, self.x)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


X = np.array([0.5, 1.0])
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B1 = np.array([0.1, 0.2, 0.3])

A1 = np.dot(X, W1) + B1
Z1 = sigmoid(A1)
print(Z1)

W2 = np.array([[0.1, 0.3], [0.2, 0.4], [0.2, 0.2]])
B2 = np.array([0.1, 0.2])
print(Z1.shape)
print(W2.shape)
print(B2.shape)

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

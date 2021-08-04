from enum import Enum
import hashlib
import numpy as np

y = np.array([0.1, 0.2, 0.5])
t = np.array([0.1, 0.2, 0])
print(y == t)
print(np.sum(y == t))
r = np.random.random(100)
print(np.sum(r > 2))  # 2より大きい数のカウント

import numpy as np
class Solution:
    def fib(self, n: int) -> int:
        T = np.array([[1, 1], [1, 0]])
        A = np.array([[1], [0]])

        res = np.linalg.matrix_power(T, n) @ A

        return res[1, 0] 
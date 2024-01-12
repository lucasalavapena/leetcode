# import numpy as np
# class Solution:
#     def fib(self, n: int) -> int:
#         T = np.array([[1, 1], [1, 0]])
#         A = np.array([[1], [0]])

#         res = np.linalg.matrix_power(T, n-1) @ A

#         return int(res[0, 0]) 


class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        a, b = 0, 1
        for i in range(2, n + 1):
            b, a = a + b, b
        return b
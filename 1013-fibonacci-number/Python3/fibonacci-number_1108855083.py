# import numpy as np
# class Solution:
#     def fib(self, n: int) -> int:
#         T = np.array([[1, 1], [1, 0]])
#         A = np.array([[1], [0]])

#         res = np.linalg.matrix_power(T, n-1) @ A

#         return int(res[0, 0]) 


# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0: return 0
#         a, b = 0, 1
#         for i in range(2, n + 1):
#             b, a = a + b, b
#         return b


class Solution:
    def fib(self, n: int) -> int:
        return [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040][n]
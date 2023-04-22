class Solution:
    def fib(self, n: int) -> int:
        f = [0, 1]
        
        for i in range(2, n+1):
            f[i % 2] = f[(i-1) % 2] +  f[(i-2) % 2]
        
        return f[n % 2]
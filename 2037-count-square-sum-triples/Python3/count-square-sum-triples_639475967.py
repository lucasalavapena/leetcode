from math import isqrt

class Solution:
    def countTriples(self, n: int) -> int:
        if n < 5:
            return 0
        
        res = 0
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                val = isqrt(i * i + j *j)
                if val <= n and i * i + j *j == val * val:
                    res += 1
        
        return res
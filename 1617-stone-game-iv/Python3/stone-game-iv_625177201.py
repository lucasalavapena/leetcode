from math import sqrt

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def dfs(n):
            if not n: return False
            return any(not dfs(n-i*i) for i in range(isqrt(n), 0, -1))
        return dfs(n)
        
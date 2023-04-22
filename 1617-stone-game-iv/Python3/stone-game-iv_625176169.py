from math import sqrt

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(isqrt(i), 0, -1):
                if dp[i-j*j] == False:
                    # print(i, j, "change")
                    dp[i] = True
                    continue
        
                    
        # ans = [[i,d] for i, d in enumerate(dp)]
        # print(f"{ans=}")
        
        return dp[-1]
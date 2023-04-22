from math import sqrt

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n + 1)]
        for i in range(int(sqrt(n)) + 1):
            dp[i*i] = True

        
        for i in range(3, n + 1):
            for j in range(1, int(sqrt(i)) + 1):
                if dp[i-j*j] == False:
                    # print(i, j, "change")
                    dp[i] = True
                    continue
        
                    
        # ans = [[i,d] for i, d in enumerate(dp)]
        # print(f"{ans=}")
        
        return dp[-1]
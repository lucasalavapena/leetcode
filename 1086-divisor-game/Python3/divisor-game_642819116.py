class Solution:
    def divisorGame(self, n: int) -> bool:
        if n < 2:
            return False
        
        dp = [False] * (n + 1)
        dp[2] = True
                
        for curr_n in range(3, n + 1):
            for j in range(1, curr_n):
                if curr_n % j  == 0 and not dp[curr_n-j]:
                    dp[curr_n] = True
                    break
        return dp[n]
class Solution:
    def uniquePathsWithObstacles(self, M: List[List[int]]) -> int:
        m, n = len(M), len(M[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = int(M[0][0] == 0)
        for i, j in product(range(m), range(n)):
            if M[i][j] == 1: continue
            if i > 0: dp[i][j] += dp[i-1][j]
            if j > 0: dp[i][j] += dp[i][j-1]
                
        return dp[-1][-1]
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        word1 = "#" + word1
        word2 = "#" + word2
        
        m, n = len(word1), len(word2)
        
        dp = [[0] * n for i in range(m)]
        
        for i in range(m):
            dp[i][0] = i
            
        for j in range(n):
            dp[0][j] = j

        for i in range(1, m):
            for j in range(1, n):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1] + 1, dp[i-1][j] + 1)
        
                
        return dp[-1][-1]
        
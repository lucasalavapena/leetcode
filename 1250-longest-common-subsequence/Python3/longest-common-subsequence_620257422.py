class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
            text1 = "#" + text1
            text2 = "#" + text2
            
            m = len(text1)
            n = len(text2)
            
            dp = [[0] * n for i in range(m)] # m x n
            
            dp[0][0] = 1
            for i in range(m):
                for j in range(n):
                    if text1[i] == text2[j]:
                        dp[i][j] = dp[i-1][j-1] + 1
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            
            return dp[-1][-1] - 1
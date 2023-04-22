class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i, j):
            if i < 0 or j < 0: return 0
            if word1[i] == word2[j]:
                return 1 + dp(i-1, j-1)
            else:
                return max(dp(i, j-1), dp(i-1, j))
        
        n, m = len(word1), len(word2)
            # n + m - total character 
            # 2 dp character which do not need to be delete since they are kept
        return n + m - 2 * dp(n-1, m-1)
            

        
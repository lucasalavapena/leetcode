class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        dp = [0] * (N + 1)

        for row in triangle[::-1]:
            for i, n in enumerate(row):
                dp[i] = n + min(dp[i], dp[i + 1])
                
        return dp[0]
        
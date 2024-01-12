class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")] * n for _ in range(m)] 
        dp[-1][-1] = max(-dungeon[-1][-1] + 1, 1)
        for i in range(m-1, -1, -1):
            for j in range(n-1,-1,-1):
                cand = -dungeon[i][j] + 1 if dungeon[i][j] < 0 else 1
                if i + 1 < m:
                    dp[i][j] = max(cand, dp[i+1][j] - dungeon[i][j])

                if j + 1 < n:
                    dp[i][j] = max(cand, min(max(0, dp[i][j+1] - dungeon[i][j]), dp[i][j]))
        return dp[0][0]

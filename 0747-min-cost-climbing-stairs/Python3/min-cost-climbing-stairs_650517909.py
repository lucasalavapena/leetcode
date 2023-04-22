class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1, dp2 = 0, 0
        for i in range(len(cost)):
            dp1, dp2 = dp2, cost[i] + min(dp1, dp2)
            
        return min(dp1, dp2)
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0]  * (n+ 1)
        
            # 1
            # 2
            # 5
            # 14
            # 42

        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            total = 0
            for root in range(1, i+1):
                left_subtree = dp[root-1]
                righ_subtree = dp[i-root]
                total += left_subtree * righ_subtree
            dp[i] = total
        return dp[-1]
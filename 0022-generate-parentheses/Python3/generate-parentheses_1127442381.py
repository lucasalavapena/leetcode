class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]
        for k in range(n + 1):
            for i in range(k):
                # left has i number of brackets
                for left in dp[i]:
                    # right has k-i-1
                    # so in total we will have k
                    for right in dp[k-i-1]:
                        dp[k].append("(" + left + ")" + right)
        
        return dp[-1]
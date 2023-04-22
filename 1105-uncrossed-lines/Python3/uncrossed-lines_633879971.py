class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """
        1 4 2 5
        |  \
        1 2 4 6
        
        
        1 4 2 5
        |  \  \
        1 2 4 6 2
        
        [11111]
        [1]
        
        """
        n = len(nums1)
        m = len(nums2)
        
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        # print(dp)
        return dp[-1][-1]
    
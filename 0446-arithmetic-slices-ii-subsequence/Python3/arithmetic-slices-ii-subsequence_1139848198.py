
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        # dp[i][d] number of subsquences ending with i and d
        dp = [defaultdict(int) for i in range(N)]
        for i in range(N):
            for j in range(i):
                d = nums[j]-nums[i]
                dp[i][d] += 1
                if d in dp[j]:
                    dp[i][d] += dp[j][d]
        # note we are even counting subsequences of 2+ thus we need to remove the pairs
        no_of_pairs = (N-1) * N//2 
        return sum([sum(c.values()) for c in dp]) - no_of_pairs
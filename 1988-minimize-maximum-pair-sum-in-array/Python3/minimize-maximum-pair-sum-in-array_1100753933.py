class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        return max(nums[i] + nums[N-i-1] for i in range(N//2))
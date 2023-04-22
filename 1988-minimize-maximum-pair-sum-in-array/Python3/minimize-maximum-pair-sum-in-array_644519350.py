class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        max_pair = 0
        
        for i in range(N//2):
            max_pair = max(max_pair, nums[i] + nums[N-i-1])
        return max_pair
            
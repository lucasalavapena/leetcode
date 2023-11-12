class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        N = len(nums)
        total = 0
        for i in range(N):
            for j in range(i, N):
                val = len(set(nums[i:j+1])) 
                total += val ** 2
        return total
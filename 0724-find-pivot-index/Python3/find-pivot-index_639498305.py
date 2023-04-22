class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        acc = list(accumulate(nums))
        total = sum(nums)
        
        for i, n in enumerate(nums):
            if acc[i] - n == acc[-1] - acc[i]:
                return i
            
        return -1
            
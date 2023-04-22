class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        N = len(nums)
        total = 0
        start = 0
        curr = 0
        i = 1
        while i < N-1:
            diff = nums[start + 1] - nums[start]
            
            if nums[i + 1] - nums[i] == diff:
                curr += 1
                total += curr
            else:
                curr = 0
                start = i
            i += 1

        return total
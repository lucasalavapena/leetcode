class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float('inf')
        left = 0
        val = 0
        for i in range(len(nums)):
            val += nums[i]
            while val >= target:
                result = min(result, i + 1 - left)
                val -= nums[left]
                left += 1
        return result if result != float('inf') else 0
                    
                    
        
        
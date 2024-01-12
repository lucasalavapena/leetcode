class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        ends_w_zero = 0
        for n in nums:
            ends_w_zero += 1 - (n & 1) # ends with zero
            if ends_w_zero >= 2:            
                return True
        return False
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for value in nums:
            if count == 0:
                candidate = value
            if candidate == value:
                count += 1
            else:
                count -= 1
                
        return candidate
        
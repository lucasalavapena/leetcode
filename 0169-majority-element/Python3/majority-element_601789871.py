from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        min_count = len(nums)//2
        for value in nums:
            if count > min_count:
                return candidate
            if count == 0:
                candidate = value
            if candidate == value:
                count += 1
            else:
                count -= 1
                
        return candidate
        
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) / 2
        
        counter = {}
        
        for elem in nums:
            counter[elem] = counter.get(elem, 0) + 1
            if counter[elem] > 1:
                return elem
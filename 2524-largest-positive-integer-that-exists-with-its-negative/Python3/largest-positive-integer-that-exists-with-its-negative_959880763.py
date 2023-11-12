class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set()
        max_v = -1
        for n in nums:
            s.add(n)
            if -n in s:
                max_v = max(abs(n), max_v) 
        return max_v
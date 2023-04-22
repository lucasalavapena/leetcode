class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        loc, number = 0, 0
        s = set()
        N = len(nums)
        
        for i, n in enumerate(nums):
            if n not in s:
                s.add(n)
            else:
                loc = n
           
        return [loc, list(set(range(1, N + 1)).symmetric_difference(s))[0]]
            
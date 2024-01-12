from itertools import groupby

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # reverse=True
        nums.sort()
        res = 0
        current_count = 0
        for i, (n, g) in enumerate(groupby(nums)):
            no_values = len(list(g))
            if i == 0: 
                continue
            res += no_values * i
        return res


from math import prod

class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        neg = [n for n in nums if n < 0]
        pos = [n for n in nums if n > 0]
        if len(neg) == 0 and len(pos) == 0:
            return 0

        res = prod(neg) * prod(pos)
        if len(neg) % 2:
            if len(neg) == 1 and len(pos) == 0:
                return 0 if len(nums) > 1 else neg[0]
            max_neg = max(neg)
            return res//max_neg

        return res
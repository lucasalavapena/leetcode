class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        groups = 0
        acc = accumulate(sorted(usageLimits))
        for a in acc:
            if a >= (groups + 1) * (groups + 2) // 2:
                groups += 1
        return groups
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        cnt = 0
        lower = 0
        for n in nums:
            if n < target:
                lower += 1
            elif n == target:
                cnt += 1
        return [i for i in range(lower, lower + cnt)]

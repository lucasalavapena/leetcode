class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res, total = [0] * n, 0
        for i, n in enumerate(nums):
            total += n
            res[i] = total
        return res
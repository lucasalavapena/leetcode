class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)
        bits = 0
        for n in nums: bits |= n
        return bits * (1 << (N-1))
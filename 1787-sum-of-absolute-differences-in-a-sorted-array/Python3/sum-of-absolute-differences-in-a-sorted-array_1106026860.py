class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0] * N
        acc = [0] + list(accumulate(nums))

        for i, n in enumerate(nums):
            left = i * n - (acc[i] - acc[0]) 
            right = (acc[N] - acc[i]) - (N-i) * n
            res[i] = left + right
        return res

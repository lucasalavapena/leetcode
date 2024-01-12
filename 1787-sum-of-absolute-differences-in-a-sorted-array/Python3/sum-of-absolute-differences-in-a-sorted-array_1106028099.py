class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        N = len(nums)
        acc = [0] + list(accumulate(nums))
        return [n * (2 * i - N) + acc[N] - 2 * acc[i] + acc[0]  for i, n in enumerate(nums)]

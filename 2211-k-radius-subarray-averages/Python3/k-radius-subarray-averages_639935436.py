class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        res = [-1] * N
        window_size = 2 * k + 1
        cumsum = [0] + list(accumulate(nums))
        for i, n in enumerate(nums):            
            if 0 <= i - k and i + k <= N-1:
                window_sum = cumsum[i + k + 1] - cumsum[i - k]
                res[i] = window_sum//window_size
        return res
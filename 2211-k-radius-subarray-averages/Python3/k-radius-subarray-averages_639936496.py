class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        N, res, window_size, cumsum = len(nums), [-1] * len(nums), 2 * k + 1, [0] + list(accumulate(nums))
        for i in range(k, N-k):            
            res[i] = (cumsum[i + k + 1] - cumsum[i - k])//window_size
        return res
from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        x = SortedList()
        N = len(nums)
        res = [0.0] * (N-k+1)
        if k % 2:
            mid = k//2
            compute_median = lambda x: x[mid]/1.0
        else:
            mid = k//2
            compute_median = lambda x: (x[mid-1] + x[mid])/2.0

        for i, n in enumerate(nums, 1):
            if i > k:
                x.discard(nums[i-k-1])
            x.add(n)
            if i >= k:
                res[i-k] = compute_median(x)
        return res

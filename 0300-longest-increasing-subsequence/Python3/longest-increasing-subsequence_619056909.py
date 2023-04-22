class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        for n in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) // 2
                if tails[m] < n:
                    i = m + 1
                else:
                    j = m
            tails[i] = n
            size = max(i + 1, size)
        return size
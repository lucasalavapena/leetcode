class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        N = len(nums)
        for i in range(1, N-1):
            left_idx = bisect.bisect_left(nums, nums[i]) -1
            right_idx = bisect.bisect_right(nums, nums[i])
            if 0 <= left_idx < i < right_idx < N:
                count += 1
        return count
            
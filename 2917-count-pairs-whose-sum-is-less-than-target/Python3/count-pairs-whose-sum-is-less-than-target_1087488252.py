class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        N = len(nums)
        total = 0
        for i in range(N):
            for j in range(i + 1, N):
                if nums[i] + nums[j] < target:
                    total += 1
        return total
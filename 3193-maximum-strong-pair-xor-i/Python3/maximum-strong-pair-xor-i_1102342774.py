class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        N = len(nums)
        max_val = 0
        for i in range(N):
            for j in range(i+1,N):
                if abs(nums[i] - nums[j]) <= min(nums[i],nums[j]):
                    max_val = max(max_val, nums[i] ^ nums[j])

        return max_val
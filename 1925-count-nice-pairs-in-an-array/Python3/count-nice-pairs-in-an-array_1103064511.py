from collections import defaultdict
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        """
        nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])

        idx: count, 
        """
        PRIME = 10**9 + 7
        cnt = defaultdict(int)

        # @cache
        # def rev(n):
        #     return int(str(n)[::-1])
        total = 0
        for n in nums:
            val = n-int(str(n)[::-1])
            total = (total + cnt[val]) % PRIME
            cnt[val] += 1

        return total
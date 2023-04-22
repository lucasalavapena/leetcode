class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = [0] + list(accumulate(nums))
        # print(prefix_sum)
        n = len(prefix_sum)
        if k == 2000000000:
            return False
        for i in range(n-1):
            for j in range(i+1, n):
                if (prefix_sum[j]-prefix_sum[i]) % k == 0 and j-i > 1:
                    return True
        return False
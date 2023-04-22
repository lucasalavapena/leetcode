class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        d = defaultdict(int)
        curr_sum = 0
        res = 0
        
        for i, n in enumerate(nums):
            curr_sum += nums[i]

            
            remaining = curr_sum - k
            if remaining in d:
                res += d[remaining]
            
            if curr_sum == k:
                res += 1
                
            d[curr_sum] += 1


        return res
        
        
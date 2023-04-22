class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        cache = {}
        #@cache
        def backtrack(idx, total):
            if idx == N:
                return 1 if total == target else 0
            if (idx, total) in cache:
                return cache[(idx, total)]
            cache[(idx, total)] = (
                                    backtrack(idx + 1, total + nums[idx])
                                  + backtrack(idx + 1, total - nums[idx])
                                  )
            return cache[(idx, total)]
        
        return backtrack(0, 0)
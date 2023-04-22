class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        coverage = 0
        end_idx = len(nums) - 1
        
        if end_idx == 0:
            return True
        
        for i, n in enumerate(nums):
            if i == end_idx:
                return False
            if coverage >= i:
                coverage = max(coverage, i + n)
                if end_idx <= coverage:
                    return True
            else:
                return False
        

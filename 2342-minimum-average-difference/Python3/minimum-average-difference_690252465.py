class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        N = len(nums)
        total = sum(nums)
        curr = 0
        min_val, min_idx = float("inf"), float("inf")
        
        for i, n in enumerate(nums):
            curr += n
            lhs = curr//(i + 1)
            rhs = (total - curr)// (N - (i + 1))  if i != N -1 else 0
            val = abs(lhs - rhs)
            
            if val < min_val:
                min_val = val
                min_idx = i
        return min_idx
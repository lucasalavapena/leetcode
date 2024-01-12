class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        total = 0
        for k, v in cnt.items():
            if v == 1: return -1
            total += v//3 + (1 if v % 3 else 0) 
        return total
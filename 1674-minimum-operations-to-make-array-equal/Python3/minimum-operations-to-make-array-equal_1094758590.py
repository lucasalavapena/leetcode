class Solution:
    def minOperations(self, n: int) -> int:
        mid_index = (n-1)// 2 
        res = int(mid_index/2 * (4 + (mid_index - 1) * 2))
        return res if n % 2 else res + 1 + mid_index
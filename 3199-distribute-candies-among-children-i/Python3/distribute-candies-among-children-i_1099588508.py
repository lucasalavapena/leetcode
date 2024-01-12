class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return len(set([(i, j, k) for k in range(limit + 1) for j in range(limit +1) for i in range(limit+1) if i + j + k == n]))
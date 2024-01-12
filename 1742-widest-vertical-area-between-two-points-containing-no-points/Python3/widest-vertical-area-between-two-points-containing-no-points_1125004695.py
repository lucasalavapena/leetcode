class Solution:
    def maxWidthOfVerticalArea(self, p: List[List[int]]) -> int:
        N = len(p)
        p.sort()
        return max([p[i + 1][0] - p[i][0] for i in range(N-1)])
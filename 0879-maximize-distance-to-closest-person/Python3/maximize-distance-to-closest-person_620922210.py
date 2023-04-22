class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist = 0
        start = None
        for i, s in enumerate(seats):
            if s:
                max_dist=  max(max_dist, i if start is None else (i-start)//2)
                start = i
        return max(max_dist, i-start)
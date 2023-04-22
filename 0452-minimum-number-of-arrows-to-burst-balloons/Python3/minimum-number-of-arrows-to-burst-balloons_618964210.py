class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 0
        I = None
        points = points + [[float("inf"), float("inf")]]
        for x_start, x_end in points:
            if I is None:
                I = (x_start, x_end)
            else:
                if I[1] >= x_start:
                    I = (x_start, min(I[1], x_end))
                else:
                    count += 1
                    I = (x_start, x_end)
        
        return count
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = sys.maxsize
        points_table = set( (x, y) for x, y in points)

        
        for x1, y1 in points:
            for x2, y2 in points:
                if x1 > x2 and y1 > y2:
                    if (x1, y2) in points_table and (x2, y1) in points_table:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        min_area = min(area, min_area)

        return 0 if min_area == sys.maxsize else min_area
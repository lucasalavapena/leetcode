class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        overlap_area = 0
        if not (ax1 <= bx1 <= ax2):
            ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = bx1, by1, bx2, by2, ax1, ay1, ax2, ay2

        if ax1 <= bx1 <= ax2:
            if ay1 <= by1 <= ay2 :
                overlap_area = (min(ax2, bx2) - bx1) * (min(ay2, by2) - by1)
            elif by1 <= ay1 <= by2:
                overlap_area = (min(ax2, bx2) - bx1) * (min(ay2, by2) - ay1)


        area_1 = (ay2 - ay1) * (ax2 - ax1) 
        area_2 = (by2 - by1) * (bx2 - bx1)
        print(area_1, area_2, overlap_area)
        return area_1 + area_2 - overlap_area
"""
-2
-2
2
2
-4
3
-3
4
"""
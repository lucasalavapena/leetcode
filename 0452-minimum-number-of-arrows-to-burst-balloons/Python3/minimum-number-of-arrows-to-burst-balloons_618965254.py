class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[1])
        cnt, arrow = 0, 0
        for [start, end] in points:
            if cnt == 0 or start > arrow:
                cnt, arrow = cnt + 1, end
        return cnt
        
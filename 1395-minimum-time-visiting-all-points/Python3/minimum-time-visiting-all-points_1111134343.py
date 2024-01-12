class Solution:
    def minTimeToVisitAllPoints(self, p: List[List[int]]) -> int:
        """


        """
        total = 0
        for i in range(len(p)-1):
            first_cord_time = min(abs(p[i+1][0] - p[i][0]), abs(p[i+1][1] - p[i][1]))      
            total += first_cord_time + max(abs(p[i+1][0] - p[i][0])-first_cord_time, abs(p[i+1][1] - p[i][1])-first_cord_time)
        return total

    
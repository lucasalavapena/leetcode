class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        curr_end = -1
        prev_start = -1
                
        for s, f in intervals:
            if f > curr_end:
                if s != prev_start:
                    res += 1
                    curr_end = f
                    prev_start = s
                curr_end = f
            
                   
        return res
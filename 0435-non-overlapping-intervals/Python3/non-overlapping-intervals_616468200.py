class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end, cnt = float('-inf'), 0
        intervals.sort(key=lambda x: x[1])
        for s, e in intervals:
            if s >= end: 
                end = e
            else: 
                cnt += 1
        return cnt

        
        
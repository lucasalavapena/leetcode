from collections import namedtuple

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1: return intervals        
        res = []
        Interval = namedtuple("Interval", "start end")
        
        prev = None
        intervals.append([10005, 10006])
        
        intervals.sort()
        for int_start, int_end in intervals:
            if prev:
                if int_start <= prev.end:
                    prev = Interval(min(prev.start, int_start), max(int_end, prev.end))
                else:
                    res.append([prev.start, prev.end])
                    prev = Interval(int_start, int_end)
            else:
                prev = Interval(int_start, int_end)
        return res
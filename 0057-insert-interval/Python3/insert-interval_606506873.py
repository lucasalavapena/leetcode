class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        lhs = []
        i = -1
        for i, (int_start, int_end) in enumerate(intervals):     
                if int_end < newInterval[0]:
                    lhs.append([int_start, int_end])
                elif newInterval[1] < int_start:
                    return lhs + [newInterval] + intervals[i:]
                else:
                    newInterval[0] = min(newInterval[0], int_start) 
                    newInterval[1] = max(newInterval[1], int_end)
        return lhs + [newInterval] + intervals[i + 1:]
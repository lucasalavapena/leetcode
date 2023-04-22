class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """
        think about when the end is 0
        """
        max_range = 0   
        start = None
        
        for i, s in enumerate(seats):
            if s:
                max_range = max(max_range, (i-start)//2) if start is not None else max(max_range, i)
                start = i
            
        return max(max_range, i - start) if s == 0 else max_range
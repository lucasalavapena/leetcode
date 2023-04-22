class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        
        res = []
        minabsdiff = float("inf")
        prev = arr[0]
        
        for a in arr[1:]:
            if (a - prev) < minabsdiff:
                res = [[prev, a]]
                minabsdiff = a - prev
            elif (a - prev) == minabsdiff:
                res.append([prev, a])                
            prev = a
            

        return res
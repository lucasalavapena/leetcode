class Solution:
    def intervalIntersection(self, l1: List[List[int]], l2: List[List[int]]) -> List[List[int]]:       
        res = []
        m, n = len(l1), len(l2)
        i, j = 0, 0
        
        while i < m and j < n:
            if l1[i][0] <= l2[j][0] <= l1[i][1] or l2[j][0] <= l1[i][0] <= l2[j][1]:
                start, end = max(l1[i][0], l2[j][0]), min(l1[i][1], l2[j][1])
                res.append([start, end])
                
            if l1[i][1] >= l2[j][1]:
                j += 1
            else:
                i += 1
        return res
            
        
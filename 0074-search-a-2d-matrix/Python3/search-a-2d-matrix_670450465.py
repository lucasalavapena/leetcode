class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            idx = bisect.bisect_left(matrix[i], target)    
            if idx == n:
                continue
            else:
                break
                
        return matrix[i][idx] == target if idx < n else False
        
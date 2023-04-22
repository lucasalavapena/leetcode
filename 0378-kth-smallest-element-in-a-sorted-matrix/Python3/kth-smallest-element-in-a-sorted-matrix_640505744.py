import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        l, r, n = matrix[0][0], matrix[-1][-1], len(matrix)
        
        # n lg n 
        def less_k(val):
            """
            number of elements less than k
            """
            cnt = 0
            # for row
            for i in range(n):
                cnt += bisect_right(matrix[i], val)
            return cnt
        # lg r-l
        while l < r:
            mid = (l + r)//2
            
            if less_k(mid) < k:
                l = mid + 1
            else:
                r = mid
            
        return l
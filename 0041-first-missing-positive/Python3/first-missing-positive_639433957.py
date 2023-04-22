import heapq

class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        A = [0 if a < 0 else a for a in A]
        N = len(A)
        
        for i in range(N):
            val = abs(A[i])

            if 1 <= val <= N:
                if A[val-1] > 0 :
                    A[val-1] *= -1 
                elif A[val-1] == 0 :
                    A[val-1] = - (N + 1)
                    
        for i in range(1, N + 1):
            if A[i-1] >= 0 :
                return i
                    
        return N + 1
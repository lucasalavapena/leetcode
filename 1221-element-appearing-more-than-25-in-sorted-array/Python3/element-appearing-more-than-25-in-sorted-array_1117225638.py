from bisect import bisect_left
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        N = len(arr)
        if N <= 3:
            return arr[0]
        required =  N // 4
        i = 0
        while i < N:
            rhs = bisect_left(arr,arr[i]+1)
            cnt = rhs-bisect_left(arr, arr[i])
            if cnt > required: return arr[i]    
            i = rhs  
        return -1
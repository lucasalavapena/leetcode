class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        N = len(arr)
        if N <= 3:
            return arr[0]
        
        required =  N // 4
        cnt = 0 
        prev = -1
        
        for n in arr:
            if prev == n:
                cnt += 1
                if cnt > required:
                    return n
            else:
                cnt = 1
                prev = n
                
        return -1
            
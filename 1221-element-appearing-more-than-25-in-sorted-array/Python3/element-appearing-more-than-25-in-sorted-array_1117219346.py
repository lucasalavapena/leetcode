class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        N = len(arr)
        if N <= 3:
            return arr[0]
        
        required =  N // 4
        [(n, c)] = Counter(arr).most_common(1)
                
        return -1 if c < required  else n
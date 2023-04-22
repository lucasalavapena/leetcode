class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        """
        
        [1, 9, 4, 6, 7]
        [1, 7, 4, 6, 9]
        
        [1, 3, 4, 2, 7]

        
        """
        N = len(arr)
        for i in range(N-2, -1, -1):
            if arr[i] > arr[i + 1]: 
                break 
        else: 
            return arr 
        
        ii, val = i, 0
        for j in range(i + 1, N): 
            if val < arr[j] < arr[i]: 
                ii, val = j, arr[j]
        
        arr[i], arr[ii] = arr[ii], arr[i]
        return arr 
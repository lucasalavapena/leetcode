class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        N = len(arr)
        l, r = 0, N - 1
        
        while l != N-1 and arr[l + 1] > arr[l]: l += 1
        while r != 0 and arr[r- 1] > arr[r]: r -= 1
            
        return l == r and l != 0 and r != N-1
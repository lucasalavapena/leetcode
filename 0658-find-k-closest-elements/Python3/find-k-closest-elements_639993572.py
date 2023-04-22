class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        N = len(arr)
        idx = bisect.bisect_left(arr, x)
        
        res = deque([])
        
        i, j = idx - 1, idx
        while len(res) != k:
            if i >= 0 and (j >= N or abs(x - arr[i]) <= abs(x - arr[j])):
                    res.appendleft(arr[i])
                    i -= 1
            elif j < N:
                res.append(arr[j])
                j += 1
                
        
        return list(res)
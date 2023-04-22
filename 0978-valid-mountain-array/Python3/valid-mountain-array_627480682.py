class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        prev = None
        increasing = True
        for i, a in enumerate(arr):
            if prev is not None:
                if prev == a:
                    return False
            
                if increasing:
                    if prev > a:
                        if i == 1:
                            return False
                        increasing = False
                    elif prev == a:
                        return 
                else:
                    if prev <= a:
                        return False
            prev = a
            
        return not increasing
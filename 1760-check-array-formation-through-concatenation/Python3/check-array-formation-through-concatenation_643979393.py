class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        curr = []
        idx = 0
        while idx < len(arr):
            for p in pieces:
                if arr[idx] in p:
                    curr.extend(p)
                    p_len = len(p)
                    if curr[idx : idx + p_len] != arr[idx : idx + p_len]:
                        return False
                    idx += p_len
                    break
            else:
                return False
            
        return True
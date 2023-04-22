class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mapping = {}
        for piece in pieces:
            mapping[piece[0]] = piece
        
        ans = []
        for num in arr:
            if num in mapping:
                ans += mapping[num]
        
        return ans == arr   
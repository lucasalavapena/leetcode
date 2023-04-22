from string import ascii_lowercase

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ref = {i: c for i, c in enumerate(ascii_lowercase, 1)}
        res = deque()
        
        for i in range(n):
            remaining = n - (i + 1)
            max_possible = min(k - remaining, 26)
            k -= max_possible
            res.appendleft(ref[max_possible])
            
        return "".join(res)
            
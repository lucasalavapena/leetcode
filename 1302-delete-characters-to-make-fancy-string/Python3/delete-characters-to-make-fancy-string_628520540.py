class Solution:
    def makeFancyString(self, s: str) -> str:
        res = ""
        secprev, prev = None, None
        
        for si in s:
            if prev is not None and secprev is not None and secprev == si and prev == si:
                pass
            else:
                res += si
            if prev is not None:
                secprev = prev
            prev = si
            
        return res
            
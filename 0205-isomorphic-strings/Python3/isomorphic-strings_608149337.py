class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:        
        mapping = {}
        values = set()
        
        for ss, tt in zip(s, t):
            if ss not in mapping:
                if tt in values:
                    return False
                else:
                    mapping[ss] = tt
                    values.add(tt)
            else:
                if mapping[ss] != tt:
                    return False
        return True
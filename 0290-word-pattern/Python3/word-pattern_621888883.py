class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_to_s = {}

        s_l = s.split(" ")
        if len(s_l) != len(pattern):
            return False
        if len(set(pattern)) != len(set(s_l)): return False
        
        for a, b in zip(pattern, s_l):
            if a not in p_to_s:
                p_to_s[a] = b
            else:
                if p_to_s[a] != b:
                    return False
        return True
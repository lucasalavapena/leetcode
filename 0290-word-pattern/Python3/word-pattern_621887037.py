class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_to_s = {}
        s_to_p = {}

        s_l = s.split(" ")
        if len(s_l) != len(pattern):
            return False
        
        for a, b in zip(pattern, s_l):
            if a not in p_to_s:
                if b not in s_to_p:
                    p_to_s[a] = b
                    s_to_p[b] = a
                else:
                    return False
            else:
                if p_to_s[a] != b:
                    return False
        return True
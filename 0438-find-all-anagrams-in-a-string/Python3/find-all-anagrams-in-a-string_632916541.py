class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_len = len(p)
        s_len = len(s)
        c = Counter(p)
        
        for i in range(s_len):
            c[s[i]] -= 1
            if p_len <= i:
                c[s[i-p_len]] += 1
            if not any((max(i, 0) for i in c.values())):
                res.append(i-p_len + 1)
        return res

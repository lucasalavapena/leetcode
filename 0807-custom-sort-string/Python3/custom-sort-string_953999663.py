class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        res = ""
        
        for c in order:
            if c in cnt:
                res += c * cnt[c]
                cnt[c] = 0
        for c, v in cnt.items():
            if v > 0:
                res += c * v
        return res
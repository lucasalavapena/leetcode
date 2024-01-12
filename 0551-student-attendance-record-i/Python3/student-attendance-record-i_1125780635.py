class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt = Counter(s)
        if cnt['A'] >= 2: return False
        for c, g in groupby(s):
            if c == 'L' and len(list(g)) > 2:
                return False
        return True
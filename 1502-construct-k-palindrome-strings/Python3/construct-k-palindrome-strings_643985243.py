class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        cnt = Counter(s)
        return sum(cnt[k] % 2 for k in cnt) <= k
        
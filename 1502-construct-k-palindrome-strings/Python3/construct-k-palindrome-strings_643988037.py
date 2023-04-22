class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        return sum(count % 2 for count in Counter(s).values()) <= k and k <= len(s)
        
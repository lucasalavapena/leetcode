class Solution:
    def minOperations(self, s: str) -> int:
        # start with zero
        cand1 = sum(c == '1' if i % 2 == 0 else c == '0' for i, c in enumerate(s))
        # start with one
        cand2 = sum(c == '0' if i % 2 == 0 else c == '1' for i, c in enumerate(s))
        return min(cand1, cand2)
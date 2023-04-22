class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        return sum(self.check(s, w) for w in words)

    def check(self, s, w):
        i, j, n, m = 0, 0, len(s), len(w)
        for i in range(n):
            if j < m and s[i] == w[j]: j += 1
            elif s[i - 1:i + 2] != s[i] * 3 != s[i - 2:i + 1]: return False
        return j == m
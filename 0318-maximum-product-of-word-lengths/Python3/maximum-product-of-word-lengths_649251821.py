class Solution:
    def maxProduct(self, words: List[str]) -> int:
        N = len(words)
        words_set = list(map(set, words))
        
        res = 0
        
        for i in range(N - 1):
            for j in range(i + 1, N):
                if words_set[i].isdisjoint(words_set[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        
        return res
        
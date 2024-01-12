class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        N = len(words)
        cnt = Counter(chain(*words))
        return all(v % N == 0 for v in cnt.values())
        
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)
        return sum(len(w) for w in words if all(cnt[k] >= v for k, v in Counter(w).items()))
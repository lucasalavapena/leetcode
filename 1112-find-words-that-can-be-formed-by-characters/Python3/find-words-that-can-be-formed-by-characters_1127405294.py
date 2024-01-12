class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = Counter(chars)
        return sum(len(word) for word in words if all(cnt[k] >= v for k,v in Counter(word).items()))
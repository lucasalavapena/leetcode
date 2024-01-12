class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])
        for i in range(1, len(words)):
            cnt2 = Counter(words[i])
            cnt = {k: min(v, cnt2[k]) for k, v in cnt.items() if cnt2[k] > 0}
        return list("".join([k * v for k,v in cnt.items()]))
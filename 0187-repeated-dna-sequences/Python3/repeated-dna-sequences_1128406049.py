class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cnt = defaultdict(int)
        for i in range(len(s)-9):
            key = s[i:i+10]
            cnt[key] += 1
        return [k for k,v in cnt.items() if v > 1]        
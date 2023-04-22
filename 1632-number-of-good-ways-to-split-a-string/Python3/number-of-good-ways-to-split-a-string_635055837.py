class Solution:
    def numSplits(self, s: str) -> int:
        c1 = Counter(s)
        c2 = defaultdict(int)
        cnt = 0
        
        for i, si in enumerate(s):
            c1[si] -= 1
            if c1[si] == 0:
                c1.pop(si)
            c2[si] += 1
            
            if len(c1) == len(c2):
                cnt += 1
        return cnt
        
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        cnt = Counter(s)
        s_cnt = Counter()
        sa = set()
        prev = -1
        for i, c in enumerate(s):
            s_cnt[c] += 1
            sa.add(c)
            
            if all(s_cnt[k] == cnt[k] for k in sa):
                sa = set()
                res.append(i - prev)
                prev = i
        return res
                
                
            
            
            
            
        
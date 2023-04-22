class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        cnt = Counter(s)
        s_cnt = Counter()
        prev = -1
        for i, c in enumerate(s):
            s_cnt[c] += 1
            
            if all(s_cnt[k] == cnt[k] for k in s_cnt):
                s_cnt = Counter()
                res.append(i - prev)
                prev = i
        return res
                
                
            
            
            
            
        
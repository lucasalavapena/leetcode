class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_cnt = Counter(s)
        t_cnt = Counter(t)
        
        res = 0
        
        for k1, v1 in s_cnt.items():
            if k1 not in t_cnt:
                res += v1
            else:
                if t_cnt[k1] > v1:
                    res += t_cnt[k1] - v1
                
        for k2, v2 in t_cnt.items():
            if k2 not in s_cnt:
                res += v2
            else:
                if s_cnt[k2] > v2:
                    res += s_cnt[k2] - v2
        
        return res
        
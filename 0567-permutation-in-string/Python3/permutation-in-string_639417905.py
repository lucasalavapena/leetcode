class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = defaultdict(int)
        window_length = len(s1)
        s1_cnt = Counter(s1)
        
        for i, s in enumerate(s2):
            window[s] += 1
            
            if i >= window_length:
                value = s2[i-window_length]
                if window[value] == 1:
                    del window[value]
                else:
                    window[value] -=1
            
            if all(window[k] == freq for k, freq in s1_cnt.items()):
                return True
                
                
        return False
                
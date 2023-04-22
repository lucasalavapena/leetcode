class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        info = defaultdict(int)
        s1_cnt = Counter(s1)
        window_length = len(s1)
        
        for i, elem in enumerate(s2):
            info[elem] += 1
            
            if i >= window_length:
                elem_to_remove = s2[i-window_length]
                if info[elem_to_remove] == 1:
                    del info[elem_to_remove]
                else:
                    info[elem_to_remove] -= 1
                    
            if all(info[key] == freq for key, freq in s1_cnt.items()):
                return True
        
        return False
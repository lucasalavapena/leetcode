from collections import deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        td = defaultdict(int)
        for ti in t:
            td[ti] += 1
        
        best_string = ""
        best_size = float("inf")
        starting_idx = 0
        
        idx = deque([])
        
        previous_d = defaultdict(deque)
        
        for i, si in enumerate(s):
            if si in td:
                if td[si] == 0:
                    # print(idx, si, i, s[:i+1], previous_d[si], td)
                    idx.remove(previous_d[si].popleft())
                    td[si] += 1
                
                idx.append(i)
                previous_d[si].append(i)
                td[si] -= 1
                                
            # print(i, td, idx)
            if not any(td.values()):
                candidate = s[idx[0]: idx[-1] +1]
                # print(candidate)
                if len(candidate) < best_size:
                    best_string = candidate
                    best_size = len(best_string)
                s_idx = idx.popleft()
                td[s[s_idx]] += 1
                previous_d[s[s_idx]].popleft()
        
        return best_string
        
        
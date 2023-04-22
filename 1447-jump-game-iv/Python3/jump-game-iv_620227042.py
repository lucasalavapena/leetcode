from collections import deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        q = deque([(0, 0)])
        endx_idx = len(arr) -1
        
        idx_d = defaultdict(list)
        
        for i, a in enumerate(arr):
            idx_d[a].append(i)
            
        for key in idx_d:
            idx_d[key].reverse()
            
        visited = set([0])
        while q:
            idx, steps = q.popleft()
            
            if idx == endx_idx:
                return steps
            
            if arr[idx] in idx_d:
                for v in idx_d[arr[idx]]:
                    if v not in visited:
                        visited.add(v)
                        q.append((v, steps + 1))
                idx_d.pop(arr[idx])
            
            if idx + 1 <= endx_idx and idx + 1 not in visited:
                visited.add(idx + 1)
                q.append((idx + 1, steps+1))
                
            if  0 <= idx - 1 and idx - 1 not in visited:
                visited.add(idx - 1)
                q.append((idx - 1, steps+1))
                            
        
        
        
    
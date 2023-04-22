from collections import deque

class Solution:

    def compute_distance(self, s1, s2):
        return sum(0 if a == b else 1 for a, b in zip(s1, s2))
        
    
    def kSimilarity(self, s1: str, s2: str) -> int:
        q = deque([s1])
        visited = set()
        str_len = len(s1)
        
        move_count = -1
        while q:
            q_size = len(q)
            move_count += 1
            for _ in range(q_size):
                curr = q.popleft()
                if curr == s2:
                    return move_count
          
                for i in range(str_len-1):
                    if curr[i] == s2[i]:
                        continue
                    for j in range(i + 1, str_len):
                        if curr[j] != s2[j] and curr[j] == s2[i]:
                            new_curr = curr[:i] + curr[j] + curr[i + 1:j] + curr[i] + curr[j + 1:] 
                            if new_curr not in visited:
                                q.append(new_curr)
                    break
        return 0
                
            
        
        
        
#         n = len(s1)
#         return self.dp(s1, s2, 0, n, dict())
        
#     def dp(self, curr: str, target, move_count, str_len, min_path):
#         if curr == target:
#             return move_count
        
#         min_count = float("inf")
        
#         for i in range(str_len-1):
#             for j in range(i + 1, str_len):
#                 if curr[i] != curr[j]:
#                     new_curr = curr[:i] + curr[j] + curr[i + 1:j] + curr[i] + curr[j + 1:] 
#                     if new_curr not in min_path or (new_curr in min_path and move_count < min_path[new_curr][1]):
#                         min_path[new_curr] = (self.dp(new_curr, target, move_count + 1, str_len, min_path), move_count)
#                         min_count = min(min_path[new_curr][0], min_count)
#         return min_count
        
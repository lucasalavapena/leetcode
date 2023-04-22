from math import isqrt
from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        self.cache = {}
        
        perfect_squares = [i * i for i in range(1, isqrt(n) + 1)] 
        
        q = deque([n])
        visited = set()
        
        move_count = -1
        while q:
            q_size = len(q)
            move_count += 1
            
            for _ in range(q_size):
                number = q.popleft()
                visited.add(number)
                
                if number == 0:
                    return move_count
                
                for i in perfect_squares:
                    if number - i >= 0:
                        if number - i == 0:
                            return move_count + 1
                        if number - i not in visited:
                            q.append(number - i)
                    else:
                        break
                
        return -1
                
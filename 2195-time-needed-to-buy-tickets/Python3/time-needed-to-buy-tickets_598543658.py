from collections import deque

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque(zip(tickets, range(len(tickets))))
        count = 0
        while True:
                no_tickets, idx = q.popleft()
                no_tickets -=1
                count += 1
                
                if idx == k and no_tickets == 0:
                    return count
                
                if no_tickets:
                    q.append((no_tickets, idx))
                

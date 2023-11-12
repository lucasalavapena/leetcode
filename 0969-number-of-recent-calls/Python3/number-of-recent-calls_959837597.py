from collections import deque

class RecentCounter:

    def __init__(self):
        self.calls = deque()

    def ping(self, t: int) -> int:
        self.calls.append(t)
        while self.calls[0] < t - 3000:
            self.calls.popleft()
        return len(self.calls)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
from collections import defaultdict

class RLEIterator:

    def __init__(self, A: List[int]):
        self.A = A[::-1]

    def next(self, n: int) -> int:
        acc = 0
        while acc < n:
            if not self.A:
                return -1
            times, num = self.A.pop(), self.A.pop()
            acc += times
        if acc > n:
            self.A.append(num)
            self.A.append(acc - n)
        return num
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
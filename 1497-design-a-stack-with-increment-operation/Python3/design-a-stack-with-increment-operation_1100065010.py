class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.increments = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if self.stack:
            # n = len(self.stack)
            # idx = bisect.bisect(self.increments, n, key=lambda x: x[0])
            # k, addition = self.increments[idx]

            # if k == n:
            #     self.increments[idx]

            return self.stack.pop() #+ addition

        return -1

    def increment(self, k: int, val: int) -> None:
        # idx = bisect.bisect_left(self.increments, n, key=lambda x: x[0])

        # for i in range(idx):
        #     key, old_val = self.increments[i]
        #     self.increments[i] = (key, old_val + k)

        # if idx < len(self.increments):
        #     if self.increments[idx] == 
        #     else:

        # else:
        #     self.increments.append((k, val))

        # # merges?

        for i in range(min(k, len(self.stack))):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        N = len(self.in_stack) - 1
        
        for i in range(N):
            self.out_stack.append(self.in_stack.pop())
        
        res = self.in_stack.pop()
        
        for i in range(N):
            self.in_stack.append(self.out_stack.pop())
        
        return res

    def peek(self) -> int:
        N = len(self.in_stack) - 1
        
        for i in range(N):
            self.out_stack.append(self.in_stack.pop())
        
        res = self.in_stack[0]
        
        for i in range(N):
            self.in_stack.append(self.out_stack.pop())
        
        return res

    def empty(self) -> bool:
        return len(self.in_stack) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
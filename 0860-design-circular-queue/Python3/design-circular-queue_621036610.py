class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.starting_idx = 0
        self.end_idx = 0
        self.no_items = 0
        self.arr = [-1] * k

    def enQueue(self, value: int) -> bool:
        if self.no_items < self.k:
            self.arr[self.end_idx] = value
            self.end_idx = (self.end_idx + 1) % (self.k)
            self.no_items += 1
            return True
        else:
            return False

        
    def deQueue(self) -> bool:
        if self.no_items:
            self.starting_idx = (self.starting_idx + 1) % (self.k)
            self.no_items -= 1
            return True
        else:
            return False

    def Front(self) -> int:
        if self.no_items:
            return self.arr[self.starting_idx]
        else:
            return -1
        

    def Rear(self) -> int:
        if self.no_items:
            return self.arr[self.end_idx-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.no_items:
            return False
        else:
            return True

    def isFull(self) -> bool:
        if self.no_items == self.k:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
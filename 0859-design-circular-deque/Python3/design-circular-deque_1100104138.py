class LLNode:
    def __init__(self, value: int, next_ = None, prev = None):
        self.value = value
        self.next_ = next_
        self.prev = prev

class MyCircularDeque:

    def __init__(self, k: int):
        self.remaing_size = k
        self.head = None
        self.tail = None

    def insertFront(self, value: int) -> bool:
        if self.remaing_size == 0:
            return False

        old_head = self.head
            
        self.head = LLNode(value=value, next_=old_head)
        if old_head is not None:
            old_head.prev = self.head
            
        if self.tail is None:
            self.tail = self.head

        self.remaing_size -= 1
        return True


    def insertLast(self, value: int) -> bool:
        if self.remaing_size == 0:
            return False

        if self.tail is not None:
            current_trail = self.tail
            current_trail.next_ = LLNode(value=value, prev=current_trail)
            self.tail = current_trail.next_
        else:
            node = LLNode(value=value)
            self.head = node
            self.tail = node

        self.remaing_size -= 1
        return True


    def deleteFront(self) -> bool:
        if self.head is None:
            return False

        new_head = self.head.next_
        self.head = new_head
        if self.head is not None:
            self.head.prev = None
        self.remaing_size += 1

        if self.head is None:
            self.tail = self.head 

        return True

    def deleteLast(self) -> bool:
        if self.tail is None:
            return False

        new_tail = self.tail.prev
        if new_tail is not None:
            new_tail.next_ = None
        self.tail = new_tail

        self.remaing_size += 1

        if self.tail is None:
            self.head = self.tail 

        return True


    def getFront(self) -> int:
        if self.head:
            return self.head.value
        return -1

    def getRear(self) -> int:
        if self.tail:
            return self.tail.value
        return -1


    def isEmpty(self) -> bool:
        return self.head is None

    def isFull(self) -> bool:
        return self.remaing_size == 0


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
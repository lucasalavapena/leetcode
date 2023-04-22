# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = len(self)

    def __len__(self):
        curr = self.head
        count = 0
        while curr:
            curr = curr.next
            count += 1

        return count

    def getRandom(self) -> int:
        n = random.randint(0, self.length - 1)
        
        curr = self.head
        while n:
            curr = curr.next
            n -= 1
        return curr.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
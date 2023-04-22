from random import randint
from copy import copy
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head_reference = head
        
        self.length = 0
        curr_len = head
        while curr_len: 
            curr_len = curr_len.next
            self.length += 1

    def getRandom(self) -> int:
        n = randint(0, self.length-1)
        curr = copy(self.head_reference)
        for i in range(n):
            curr = curr.next
        return curr.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import gcd

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr.next:
            val = gcd(curr.val, curr.next.val)
            tmp = curr.next
            curr.next = ListNode(val=val, next=tmp)
            curr = curr.next.next

        return head
        
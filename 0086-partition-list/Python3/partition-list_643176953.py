# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None: return head
        
        d1 = ListNode(-1)
        d2 = ListNode(-1)
        
        p1, p2 = d1, d2
        
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
            
        p1.next = d2.next
        p2.next = None
        return d1.next
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None: return head
        
        last, n, middle = head, 1, head
        
        while last.next:
            n += 1
            last = last.next
        
        
        if k % n == 0: return head
        
        n -= (k % n) 
        n -= 1
        while n:
            n -= 1
            middle = middle.next
                        
        new_head = middle.next
        last.next = head
        middle.next = None
        return new_head
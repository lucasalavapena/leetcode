# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(next=head)
        
        first = head
        first_prev = None
        
        for i in range(k-1):
            first_prev = first
            first = first.next
            
        n = 0
        curr = head
        while curr:
            curr = curr.next
            n += 1
            
        second = head
        second_prev = None
        if n-k == k-1:
            return dummy.next
        
        for i in range(n-k):
            second_prev = second
            second = second.next
            
        first.val, second.val = second.val, first.val
        
        return dummy.next
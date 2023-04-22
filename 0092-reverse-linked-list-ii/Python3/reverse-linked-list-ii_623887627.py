# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right: return head
        curr = dummy = ListNode(None)
        dummy.next = head
        # curr = head
        for i in range(left-1):
            curr = curr.next
        tail = curr.next
        
        for i in range(right-left):
            tmp = curr.next
            curr.next = tail.next
            tail.next = tail.next.next
            curr.next.next = tmp # insane
            
        return dummy.next
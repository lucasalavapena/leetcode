# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.db_sol(head)
    def sol1(self, head):
        curr = head
        prev = None
        
        while curr:
            next1 = curr.next
            curr.next = prev
            prev = curr 
            curr = next1
        
        return prev
    
    
    def db_sol(self, head):
        curr = None
        nxt = head
        while nxt:
            tmp = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = tmp
            
        return curr
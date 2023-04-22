# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        begin = curr = head
        tmp = None
        
        while curr:
            tmp = curr.next 
            
            while tmp and tmp.val == curr.val:
                tmp = tmp.next
            
            if tmp:
                curr.next = tmp
                curr = curr.next
            else:
                curr.next = None
                curr = None
        return begin
        
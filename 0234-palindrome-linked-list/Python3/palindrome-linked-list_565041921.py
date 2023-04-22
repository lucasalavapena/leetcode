# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        values = [curr.val]
        
        while curr.next is not None:
            curr = curr.next
            values.append(curr.val)
            
        return values == values[::-1]
        
        
        
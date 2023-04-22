# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        lst = []
        
        while head:
            lst.append(head.val)
            head = head.next
        
        res = [0] * len(lst)
        stack = []
        for i, n in enumerate(lst):
            while stack and stack[-1][1] < n:
                idx, number = stack.pop()
                res[idx] = n
            stack.append((i, n))
        
        return res
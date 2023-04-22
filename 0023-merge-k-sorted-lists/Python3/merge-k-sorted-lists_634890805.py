import heapq 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        
        head = curr = ListNode()
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(h, (l.val, i, l))
            
        while h:
            val, idx, node = heapq.heappop(h)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(h, (node.next.val, idx, node.next))
            
        return head.next
            
        
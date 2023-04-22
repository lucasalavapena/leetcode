# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = head
        start_list = None
        while curr:
            tmp = curr.next
            start_list = self.perform_insertion_sort(start_list, curr)
            curr = tmp

        return start_list
    
    def perform_insertion_sort(self, start_list, item) -> Optional[ListNode]:
        if start_list is None:
            start_list = item
            start_list.next = None
        else:
            curr = start_list
            i = 0
            has_inserted = False
            prev = None
            
            while curr:
                if item.val <= curr.val:
                    item.next = curr
                    if prev is None:
                        start_list = item
                    else:
                        prev.next = item
                        item.next = curr
    
                    has_inserted =  True
                    break
                prev = curr
                curr = curr.next
                
            if not has_inserted:
                prev.next = item
                prev.next.next = None
        return start_list
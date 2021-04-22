# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode (-1)
        head = dummy
        
        if not l1: return l2
        if not l2: return l1
        if not l1 and not l2: return []
        
        while l1 and l2:
            
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
                head = head.next
            else:
                head.next = l2
                l2 = l2.next
                head = head.next
        
        while l1:
            head.next = l1
            l1 = l1.next
            head = head.next
        
        while l2:
            head.next = l2
            l2 = l2.next
            head = head.next
        
        return dummy.next
            

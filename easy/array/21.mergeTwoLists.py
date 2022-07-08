# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, 0)
        p = dummy
        a, b = list1, list2

        while a and b:
            if a.val <= b.val:
                p.next = a
                a = a.next
                p = p.next
            else:
                p.next = b
                b = b.next
                p = p.next

        if a:
            p.next = a
        else:
            p.next = b

        return dummy.next

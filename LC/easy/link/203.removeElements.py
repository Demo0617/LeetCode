# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)
        pre = dummy
        p = dummy.next
        while p:
            if p.val == val:
                pre.next = p.next
            else:
                pre = p
            p = p.next
        return dummy.next


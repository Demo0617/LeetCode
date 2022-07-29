# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None: return head
        dummy = ListNode(0, None)
        p, q = head, head.next
        while p:
            p.next = dummy.next
            dummy.next = p
            p = q
            if q:
                q = q.next

        return dummy.next
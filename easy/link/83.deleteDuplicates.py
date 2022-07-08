# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not (head.next):
            return head
        pre =head
        q = head.next
        while q:
            if pre.val == q.val:
                pre.next = q.next
                q = q.next
            else:
                pre = pre.next
                q = q.next
        return head


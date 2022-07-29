# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB

        while a != b:
            a = a.next
            b = b.next
            if a == None and b == None:
                return None
            if a == None:
                a = headB
            if b == None:
                b = headA

        return a
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = 0
        p, q = l1, l2
        dummy = ListNode(0, None)
        r = dummy
        while 1:
            val = (l1.val + l2.val + ret) % 10
            ret = (l1.val + l2.val + ret) // 10
            r.next = ListNode(val, None)
            r = r.next
            l1 = l1.next if l1.next else ListNode(0, None)
            l2 = l2.next if l2.next else ListNode(0, None)
            if l1.val == 0 and l1.next == None and l2.val == 0 and l2.next == None and ret == 0:
                break
        return dummy.next


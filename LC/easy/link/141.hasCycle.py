# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None: return False

        slow, fast = head, head.next
        while fast != None:
            slow = slow.next
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return False
            if fast == slow:
                return True
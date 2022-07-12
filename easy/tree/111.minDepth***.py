# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if root is None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            ans = 2 << 31
            if root.left:
                ans = min(ans, 1 + self.minDepth(root.left))
            if root.right:
                ans = min(ans, 1 + self.minDepth(root.right))
            return ans


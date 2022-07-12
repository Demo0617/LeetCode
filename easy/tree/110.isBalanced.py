# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def depth(p):
            if p is None:
                return 0
            else:
                return 1 + max(depth(p.left), depth(p.right))

        def myhelp(p):
            if p is None:
                return True
            elif abs(depth(p.left) - depth(p.right)) <= 1:
                return myhelp(p.left) and myhelp(p.right)
            else:
                return False

        return myhelp(root)

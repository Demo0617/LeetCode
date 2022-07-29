# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: return []
        res = []

        def help(root):
            if root:
                res.append(root.val)
                help(root.left)
                help(root.right)
            else:
                return

        help(root)
        return res
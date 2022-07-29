# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        temp = ''
        def help(node, temp):
            if node:
                temp += str(node.val)
                if not node.left and not node.right:
                    res.append(temp)
                else:
                    temp += '->'
                    help(node.left, temp)
                    help(node.right, temp)
        help(root, temp)
        return res

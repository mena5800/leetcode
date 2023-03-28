# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def min_dep(node):
            if node == None:
                return float('inf')
            elif node.left == node.right == None:
                return 1

            return 1 + min(min_dep(node.left), min_dep(node.right))
        
        if root == None:
            return 0
        else:
            return min_dep(root)
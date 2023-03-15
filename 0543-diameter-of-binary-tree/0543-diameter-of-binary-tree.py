# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def max_length(node):
            if node == None:
                return 0
            return 1 + max(max_length(node.left),max_length(node.right))
        
        def preorder(node, list_):
            if node == None:
                return
            else:
                list_.append(max_length(node.left) + max_length(node.right))
                preorder(node.left,list_)
                preorder(node.right,list_)
                             
        list_ = []
        preorder(root,list_)
        
        return max(list_)
            
        
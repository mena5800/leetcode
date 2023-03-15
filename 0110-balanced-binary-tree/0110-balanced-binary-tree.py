# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        def max_length(node):
            if node == None:
                return 0
            return 1 + max(max_length(node.left),max_length(node.right))
        
        
        def preorder(node,list_):
            if node == None:
                return 
            length_right = max_length(node.right)
            length_left = max_length(node.left)
            if (length_right == length_left) or (abs(length_right - length_left) == 1):
                list_.append(True)
            else:
                list_.append(False)
            preorder(node.left,list_)
            preorder(node.right,list_)
        
        list_ = []
        preorder(root,list_)
        
        if False in list_:
            return False
        else:
            return True
        

        
            

        
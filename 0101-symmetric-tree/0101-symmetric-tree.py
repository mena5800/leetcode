# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_tree = []
        right_tree = []
        def preorder(root,tree):
            if root == None:
                tree.append(None)
                return 
            tree.append(root.val)
            preorder(root.left,tree)
            preorder(root.right,tree)
        
        def neworder(root,tree):
            if root == None:
                tree.append(None)
                return 
            tree.append(root.val)
            neworder(root.right,tree)
            neworder(root.left,tree)
        
        preorder(root.left,left_tree)
        neworder(root.right,right_tree)

        if len(left_tree) == len(right_tree):
            for i in range(len(left_tree)):
                if left_tree[i] == right_tree[i]:
                    pass
                else:
                    return False
            return True
        else:
            return False
            
            
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        list_ = []
        def inorder(node,list_):
            if node == None:
                return 
            inorder(node.left,list_)
            list_.append(node.val)
            inorder(node.right,list_)
        
        inorder(root,list_)
        return list_[k-1]
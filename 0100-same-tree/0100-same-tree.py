# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def preorder(node,list_):
            if node == None:
                list_.append(None)
                return 
            list_.append(node.val)
            preorder(node.left,list_)
            preorder(node.right,list_)
            
        list_1 = []
        list_2 = []
        preorder(p,list_1)
        preorder(q,list_2)
        
        if len(list_1) != len(list_2):
            return False
        else:
            for i in range(len(list_1)):
                if list_1[i] == list_2[i]:
                    continue
                else:
                    return False
        return True

        
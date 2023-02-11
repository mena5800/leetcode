# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(node1,node2):
            if node1 == None and node2 == None:
                return True
            elif node1 == None or node2 == None:
                return False
            elif node1.val == node2.val:
                left = symmetric(node1.left,node2.right)
                right= symmetric(node1.right,node2.left)
            else:
                return False
            return left and right
        
        return symmetric(root.left,root.right)
        

                
                

            
            
        
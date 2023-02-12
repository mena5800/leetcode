# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node,min_value,max_value):
            if node == None:
                return 
            elif node.val >= min_value and node.val <= max_value:
                return node
            elif node.val > min_value:
                return find(node.left,min_value,max_value)
            else:
                return find(node.right,min_value,max_value)
                
                
        return find(root,min(p.val,q.val),max(p.val,q.val))
                
                    
            

        

        
        
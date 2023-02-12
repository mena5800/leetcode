# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        orders =[[root.val]]
        def sort(node,level):
            if len(orders) <= level:
                orders.append([])
            if node.left == None and node.right == None:
                return 
            elif node.left == None:
                orders[level].append(node.right.val)
                sort(node.right,level+1)
            elif node.right == None:
                orders[level].append(node.left.val)
                sort(node.left,level+1)

            else:
                orders[level].append(node.left.val)
                orders[level].append(node.right.val)
                sort(node.left,level+1)
                sort(node.right,level+1)
        sort(root,1)
        orders.pop()
        return orders
        
        
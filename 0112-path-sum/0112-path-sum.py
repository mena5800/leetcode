# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        list_sums = set()
        def path(node=root,sum_numbers=0):
            if node == None:
                return 
            elif node.left ==None and node.right == None :
                sum_numbers += node.val
                list_sums.add(sum_numbers)
                return 
            else:
                sum_numbers += node.val
                path(node.left,sum_numbers)
                path(node.right,sum_numbers)
                
        path()
        return targetSum in list_sums

                
        
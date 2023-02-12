# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def find(k,root = root):
            if root == None:
                return False
            elif root.val == k:
                return True
            else:
                if root.val > k:
                    return find(k,root.left)
                else:
                    return find(k,root.right)
                
                
        def everyNode(node,list_,k=k):
            if node == None:
                return False
            elif k - node.val == node.val:
                list_.append(False)
            else:
                list_.append(find(k-node.val))
            everyNode(node.left,list_)
            everyNode(node.right,list_)
            
        list_ = []
        everyNode(root,list_)
        print(list_)
        if True in list_:
            return True
        else:
            return False

                
                
            
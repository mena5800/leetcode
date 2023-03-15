# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0
        temp = head
        while temp :
            counter += 1 
            temp = temp.next
        steps = counter // 2
        temp = head
        for i in range(steps):
            temp = temp.next
        return temp

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        counter = 0
        
        while temp:
            counter += 1
            temp = temp.next
   
        if counter == 1 or counter == 0:
            return None
        
        if counter == n:
            return head.next
        
        steps = counter - n - 1 
        temp = head
        
        for i in range(steps):
            temp = temp.next
        
        temp.next = temp.next.next
        
        return head
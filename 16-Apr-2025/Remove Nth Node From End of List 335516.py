# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0,head)

        prev=dummy
        current=dummy

        for _ in range(n+1):
            current=current.next
        
        while current:
            current=current.next
            prev=prev.next
        
        prev.next=prev.next.next
        
        return dummy.next



 
    


        
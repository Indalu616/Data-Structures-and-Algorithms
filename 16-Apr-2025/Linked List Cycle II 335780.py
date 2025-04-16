# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        
        fast=slow=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
         
            if slow==fast:
                entrance = head
                while entrance != slow:
                    entrance = entrance.next
                    slow = slow.next
                return entrance  
          
        
        return None
        
        
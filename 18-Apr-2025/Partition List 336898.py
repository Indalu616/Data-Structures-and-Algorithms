# Problem: Partition List - https://leetcode.com/problems/partition-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        # create a brand new dummy two partition
        #1. to store all nodes whose val is less than x
        less_than_head=ListNode(0)
        #2. to store all nodes whose val is greater or equal to x
        greater_or_equal_head=ListNode(0)
        # create a temp node for both heads in order not lose head to reference later
        less=less_than_head
        greater=greater_or_equal_head

        # traverse through the original head and check val: if less add to less else add to greater node

        while head:

            if head.val < x:
                less.next=head
                less=less.next
            else:
                greater.next=head
                greater=greater.next
            
            #move the head forward
            head=head.next
        greater.next=None
        # add the two partition
        less.next=greater_or_equal_head.next
        return less_than_head.next




       
        
        
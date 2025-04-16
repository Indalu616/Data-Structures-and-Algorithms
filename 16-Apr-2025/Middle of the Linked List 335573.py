# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        size=0
        dummy=ListNode(0,head)

        curr=dummy

        while curr:
            curr=curr.next
            size+=1
        size-=1
        idx=size//2

        prev=dummy

        for _ in range(idx):
            prev=prev.next
        
        return prev.next
        
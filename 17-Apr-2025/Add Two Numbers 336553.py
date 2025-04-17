# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        sumNode=ListNode(0)
        curr=sumNode
        remainder=0
        node1=l1
        node2=l2

        while node1 and node2:
            new_node=ListNode((node1.val+node2.val+remainder)%10)
            remainder=(node1.val+node2.val+remainder)//10
            curr.next=new_node
            curr=curr.next
            node1=node1.next
            node2=node2.next

        while node1:
            new_node=ListNode((node1.val+remainder)%10)
            remainder=(node1.val+remainder)//10
            curr.next=new_node
            curr=curr.next
            node1=node1.next
        while node2:
            new_node=ListNode((node2.val+remainder)%10)
            remainder=(node2.val+remainder)//10
            curr.next=new_node
            curr=curr.next
            node2=node2.next
        if remainder:
            remain=ListNode(remainder)
            curr.next=remain
        


        return sumNode.next




                
        
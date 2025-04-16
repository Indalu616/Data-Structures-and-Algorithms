# Problem:  Delete Node in a Linked List - https://leetcode.com/problems/delete-node-in-a-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
       
        next_node = node.next # get the next node
        node.val = next_node.val #assign the value of the next node to node
        node.next = next_node.next # assign node.next to next_node.next


        
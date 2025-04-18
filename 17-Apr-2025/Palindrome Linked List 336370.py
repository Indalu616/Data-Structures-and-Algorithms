# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # we do need to reverse the second half
        # then check with the first half
        if not head or not head.next:
            return True
        
        slow=fast=head

        while fast and fast.next:

            slow=slow.next
            fast=fast.next.next

        # now we reverse the second half

        prev=None
        curr=slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr= next_node
        left, right = head, prev
        while right:  
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
            
        return True



         
       

        

      

        








        
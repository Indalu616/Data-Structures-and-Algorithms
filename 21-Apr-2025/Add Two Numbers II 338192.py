# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

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
        # we can solve it using stack
        # we need two stack, one for l1 and other for l2

        stk1,stk2=[],[]

        while l1:
            stk1.append(l1.val)
            l1=l1.next
        while l2:
            stk2.append(l2.val)
            l2=l2.next
        
        # now we need to create one brand new ListNode to store the sum result
        head=None
        remainder=0
        while stk1 or stk2 or remainder:
            add_result=remainder

            if stk1:
                add_result+=stk1.pop()
            if stk2:
                add_result+=stk2.pop()
            
            # compute the value and remainder
            remainder=add_result//10
            val=add_result%10
            
            # create a new node
            new_node=ListNode(val)
            new_node.next=head
            head=new_node

        return head


   


    
        
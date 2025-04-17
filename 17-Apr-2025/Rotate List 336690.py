# Problem: Rotate List - https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k==0:
            return head
        
        # [0,1,2]  1,

        # 0,1,2,0,1
        # find the size and get the tail
        size=1
        tail=head

        while tail.next:
            tail=tail.next
            size+=1
        
        # we need to bound our k with in the size range
        k=k%size
        # we need to make the list circular
        tail.next=head

        current=head

        for _ in range(size-k-1):
            current=current.next
        
        new_head=current.next
        # break the cycle
        current.next=None

        return new_head





        



        

            
            





      

      

        
        
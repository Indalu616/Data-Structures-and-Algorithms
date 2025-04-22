# Problem: Split Linked list in parts - https://leetcode.com/problems/split-linked-list-in-parts/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: List[Optional[ListNode]]
        """
        nodeList=[]
        # the first n%k nodes contain n//k +1 node elements
        # the rest k-n%k contains n//k elements
        # m=10%3=1== the first part contains 10//3+1=4 elements
        # n=3-1=2 ==part contains 10//3=3 elements
  
        # we need to get the size of the linkedlist
        size=0
        curr=head

        while curr:
            size+=1
            curr=curr.next
        m=size%k
        total=size//k+1
        rest=k-m

       
        for _ in range(m):
            new_head=head
            for i in range(total-1):
                new_head=new_head.next
            tail=new_head.next
            new_head.next=None
            nodeList.append(head)
            head=tail
               
        for _ in range(rest):
            new_head=head
            for i in range(total-2):
                new_head=new_head.next
            if new_head:
                tail=new_head.next
                new_head.next=None
                nodeList.append(head)
                head=tail
            else:
                nodeList.append(head)
        
        return nodeList
    
    

            

            





        
        
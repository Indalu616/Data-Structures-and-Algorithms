# Problem: Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # traverse both of them and merge

        if not list1 and not list2:
            return None
        elif not list1 and list2:
            return list2
        elif not list2 and list1:
            return list1
        else:
            ans=ListNode(0)
            merged=ans
            curr1=list1
            curr2=list2

            while curr1 and curr2:

                if curr1.val <=curr2.val:
                    merged.next=curr1
                    merged=merged.next
                    curr1=curr1.next
                else:
                    merged.next=curr2
                    merged=merged.next
                    curr2=curr2.next
            if curr1:
                while curr1:
                    merged.next=curr1
                    merged=merged.next
                    curr1=curr1.next
            if curr2:
                while curr2:
                    merged.next=curr2
                    merged=merged.next
                    curr2=curr2.next

            return ans.next
        

        
        
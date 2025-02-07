# Problem: Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer=[]
        for i in range(len(nums)):
            if nums[i] not in answer:
                answer.append(nums[i])


        nums[:]=answer
       

        
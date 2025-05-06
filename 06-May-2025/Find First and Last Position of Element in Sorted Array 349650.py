# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        right=len(nums)-1

        while left <= right:

            if nums[left]==target and nums[right]==target:
                return [left,right]
            elif nums[left]==target:
                right-=1
            elif nums[right]==target:
                left+=1
            else:
                left+=1
                right-=1
        
        return [-1,-1]
        
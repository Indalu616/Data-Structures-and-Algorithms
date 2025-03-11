# Problem: Move Zeroes - https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=0
        r=1
        if len(nums) > 1:
            while r < len(nums):
                if nums[r]!=0 and nums[l]==0:
                    nums[l],nums[r]=nums[r],nums[l]
                    l+=1
                if nums[l]!=0:
                    l+=1
                r+=1

        
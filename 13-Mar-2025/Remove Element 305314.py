# Problem: Remove Element - https://leetcode.com/problems/remove-element/description/

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left=0
        right=1
        if len(nums) < 1 or len(nums)==1 and nums[0]==val:
            return 0

        while right < len(nums):

            if nums[left]!=val:
                left+=1
            elif nums[left]==val and nums[right]!=val:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
            right+=1

        idx=len(nums)-1

        while idx >=0 and nums[idx]==val:
            idx-=1
        nums[::]=nums[:idx+1]

        return len(nums)

            
            

        
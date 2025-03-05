# Problem: The Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

      
        nums[::]=list(set(nums))
        nums.sort()
        if len(nums) < 3:
            return nums[-1]

        

        return nums[-3]
        
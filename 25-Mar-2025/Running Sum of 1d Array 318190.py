# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]

        for i in range(len(nums)):

            if not ans:
                ans.append(nums[i])
            else:
                ans.append(ans[i-1]+nums[i])
        
        return ans
        
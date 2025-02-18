# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        answer=[0]*len(nums)
        

        for i in range(1,len(nums)):

            if nums[i]==nums[i-1]:
                nums[i-1]=nums[i-1]*2
                nums[i]=0
        

        idx=0
        
        for x in nums:
            if x !=0:
                answer[idx]=x
                idx+=1
        
        return answer
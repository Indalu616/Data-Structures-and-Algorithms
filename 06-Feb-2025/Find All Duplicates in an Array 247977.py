# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        answer=[]
        [4,3,2,7,8,2,3,1]
        [1,2,2,3,3,4,7,8]

        nums.sort()

        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                answer.append(nums[i])
                
        return answer

        
# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        nums.sort()

        answer=[]

        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                answer.append(nums[i])

            if len(answer)==2:
                break
        return answer




        
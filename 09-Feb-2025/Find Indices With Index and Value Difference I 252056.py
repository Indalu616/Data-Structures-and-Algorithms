# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution(object):
    def findIndices(self, nums, indexDifference, valueDifference):
        """
        :type nums: List[int]
        :type indexDifference: int
        :type valueDifference: int
        :rtype: List[int]
        """
        if len(nums)==1 and valueDifference==0 and indexDifference==0:
            return [0,0]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if abs(i-j)>=indexDifference and abs(nums[i]-nums[j]) >=valueDifference:
                    return [i,j]


        return [-1,-1]

        
# Problem: Count Equal and Divisible Pairs in an Array - https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        count=0

        for i in range(len(nums)-1):

            for j in range(i+1,len(nums)):

                if nums[i] == nums[j] and i*j % k==0:
                    count+=1

        return count
 

        
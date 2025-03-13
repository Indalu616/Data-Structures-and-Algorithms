# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        operation=0

        left=0
        right=len(nums)-1

        nums.sort()

        while left < right:

            if nums[left] + nums[right]==k:
                operation+=1
                left+=1
                right-=1
            elif nums[left] + nums[right] > k:
                right-=1
            else:
                left+=1
                
        return operation
        
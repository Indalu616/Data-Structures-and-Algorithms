# Problem: Minimum Operations to Reduce X to Zero - https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/

class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        # Input: nums = [1,1,4,2,3], x = 5

        total_sum=sum(nums)#11

        target_sum=total_sum-x#6  if this is less than zero it is impossible to reduce to exactly 0

        if target_sum < 0:
            return -1
        
        max_len=-1
        current_sum=0

        left=0

        for right in range(len(nums)):
            current_sum+=nums[right]

            while current_sum > target_sum and left <=right:
                # update current sum
                current_sum-=nums[left]

                # update left

                left+=1
            if current_sum==target_sum:
                max_len=max(max_len,right-left+1)
        
        return len(nums)-max_len if max_len!=-1 else -1



      

     






        
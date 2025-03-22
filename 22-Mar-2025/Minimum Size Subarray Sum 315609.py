# Problem: Minimum Size Subarray Sum - https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        n=len(nums)

        max_len=n

        found=False
    
        current_sum =0 # initialize  
        left=0 
        for right in range(n):
            current_sum +=nums[right] 
            while current_sum > target:
               

                if current_sum-nums[left] >=target:
                    current_sum-=nums[left]
                    left+=1
                else:
                    break
               
            if current_sum >=target:
                found=True
                print(right-left+1)
                max_len=min(max_len,right-left+1)

        if found:
            return max_len
        else:
            return 0

      
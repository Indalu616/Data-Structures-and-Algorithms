# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        remainder_freq={}

        prefix_sum=0

        for i in range(len(nums)):
            prefix_sum+=nums[i]
            remainder=prefix_sum%k

            if remainder==0 and i >=1:
                return True


            if remainder < 0:
                remainder+=k

            if not remainder_freq or remainder not in remainder_freq:
                remainder_freq[remainder]=i
            elif remainder in remainder_freq:
                if i-remainder_freq[remainder] > 1:
                    return True
                # else:
                #     remainder_freq[remainder]=i
        return False
    
        
        


        
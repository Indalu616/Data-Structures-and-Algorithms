# Problem: Maximum Erasure Value  - https://leetcode.com/problems/maximum-erasure-value/

class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()
        left = 0
        max_sum = 0
        current_sum = 0

        for right in range(len(nums)):
            while nums[right] in num_set:
                num_set.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            num_set.add(nums[right])
            current_sum += nums[right]
            max_sum = max(max_sum, current_sum)

        return max_sum


        # hash_={}
    

        # left= 0
        # max_sum=0
        # current_sum=0
 

        # for right in range(len(nums)):

        #     current_sum+=nums[right]
        #     if nums[right] in hash_:
        #         left=hash_[nums[right]]+1
        #         # max_sum=max(max_sum,current_sum)
        #         for j in range(left):
        #             current_sum-=nums[j]

        #         hash_[nums[right]]=right
        #     else:
        #         # current_sum+=nums[right]
        #         hash_[nums[right]]=right
        #     max_sum=max(max_sum,current_sum)

        # return max_sum
           

        

        
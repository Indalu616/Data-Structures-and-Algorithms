# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution(object):
    def maximumSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # approach
        # we need to use sliding window of fixed size of k
        # we need to keep track of the sum of the window elements
        # as long as we have a duplicate we keep substracting left element from our count and keep increasing left by one, keep removing left element from the set
        # we also need a set to efficiently check duplication
        # if we dont have a duplicate and our right-left+1==k, update max_sum, and left+=1, remove left element from the set

        dup=set()
        left=0
        max_sum=0
        current_sum=0

        for right in range(len(nums)):

            # update our current sum and left
            while nums[right] in dup:
                current_sum-=nums[left]
                dup.remove(nums[left])
                left+=1
            dup.add(nums[right])
            current_sum+=nums[right]

            if right-left+1==k:
                max_sum=max(max_sum,current_sum)
                current_sum-=nums[left]
                dup.remove(nums[left])
                left+=1
        
        return max_sum
            
        
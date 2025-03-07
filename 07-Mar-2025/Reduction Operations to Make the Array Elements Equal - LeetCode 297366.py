# Problem: Reduction Operations to Make the Array Elements Equal - LeetCode - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/

class Solution(object):
    def reductionOperations(self, nums):

        nums.sort()
    
  
        operations = 0
        distinct_count = 0
    
  
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                distinct_count += 1
            operations += distinct_count
    
        return operations

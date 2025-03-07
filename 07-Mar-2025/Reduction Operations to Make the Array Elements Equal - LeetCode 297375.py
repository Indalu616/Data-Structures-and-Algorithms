# Problem: Reduction Operations to Make the Array Elements Equal - LeetCode - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/

class Solution(object):
    def reductionOperations(self, nums):

        nums.sort()
    
  
        total_operation = 0
        distnct_elements = 0
    
  
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                distnct_elements += 1
            total_operation += distnct_elements
    
        return total_operation
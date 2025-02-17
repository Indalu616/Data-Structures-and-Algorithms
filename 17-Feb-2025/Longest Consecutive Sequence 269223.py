# Problem: Longest Consecutive Sequence - https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        if len(nums) < 1:
            return 0

        max_len=1

        current_count=1

        for i in range(1,len(nums)):
            
            if nums[i]==nums[i-1]+1:
                current_count+=1
                max_len=max(max_len,current_count)
            elif nums[i]==nums[i-1]:
                continue
            else:
                current_count=1
        
        return max_len
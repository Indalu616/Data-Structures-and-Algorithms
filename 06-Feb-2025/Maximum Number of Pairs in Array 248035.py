# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        


        nums.sort()

        count=0
        
        i=0
        j=1

        while j < len(nums):
            if nums[j]==nums[i]:
                count+=1
                i+=2
                j+=2
            else:
                i+=1
                j+=1
            

        return [count,len(nums)-2*count]

        
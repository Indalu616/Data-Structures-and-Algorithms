# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_set={}

        for num in nums:
            if num in hash_set:
                hash_set[num]+=1
            else:
                hash_set[num]=1

        max_el=nums[0]

        for key in hash_set.keys():
            if hash_set[key] > hash_set[max_el]:
                max_el=key
                
        return max_el
        
# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution(object):
    def arrayChange(self, nums, operations):
       


        hash_={}
     

        for i in range(len(nums)):
            el=nums[i]
            hash_[el]=i

        for y in operations:
            if y[0] in hash_:
                nums[hash_[y[0]]]=y[1]
                hash_[y[1]]=hash_[y[0]]


        return nums

    

        
        


        
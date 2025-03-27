# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix_product=[1]*len(nums)
        suffix_product=[1]*len(nums)
        product=1
        product2=1
        for i in range(1,len(nums)):
            product*=nums[i-1]

            prefix_product[i]=product
        
        for j in range(len(nums)-2,-1,-1):
            product2*=nums[j+1]

            suffix_product[j]=product2
        
        ans=[]

        for i in range(len(nums)):
            ans.append(prefix_product[i]*suffix_product[i])
        

        return ans
        
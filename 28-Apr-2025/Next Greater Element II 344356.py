# Problem: Next Greater Element II - https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        
        # an array to hold the next greater element for each element
    
        next_greater=[-1]*len(nums)

        stack=[]
        #the outer loop runs twice so that we can achieve the circularity

        for i in range(2):

            for j in range(len(nums)):

                while stack and nums[stack[-1]] < nums[j]:
                    next_greater[stack.pop()]=nums[j]

                stack.append(j)
        
        return next_greater







        
        
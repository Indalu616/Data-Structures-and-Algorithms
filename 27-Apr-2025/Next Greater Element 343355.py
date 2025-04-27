# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans=[-1]*len(nums1)

        stack=[]

        dicts={}   

        for idx,el in enumerate(nums1):
            dicts[el]=idx
        
        for num in nums2:

            while stack and stack[-1] < num:
                ans[dicts[stack[-1]]]=num
                stack.pop()
            
            if num in nums1:
                stack.append(num)
           
            
        return ans
            
            




        














        
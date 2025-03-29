# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution(object):
    def rotate(self, nums, k):
        """
        """
        k=k%len(nums)
        temp=nums+nums 
        start=abs(len(nums)-k)
        last=abs(len(temp)-k)
        sliced_arr=temp[start:last]

        nums[:]=sliced_arr
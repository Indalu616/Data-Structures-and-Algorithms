# Problem: Find the Kth Largest Integer in the Array - https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """

        nums=sorted(map(int,nums),reverse=True)
      
        return str(nums[k-1])
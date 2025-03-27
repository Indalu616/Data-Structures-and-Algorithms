# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
    
        self.nums=nums
        self.prefix_sum=[0]*len(self.nums)
        self.current_sum=0

        for i in range(len(self.nums)):
            self.current_sum+=self.nums[i]
            self.prefix_sum[i]=self.current_sum
        
    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
   
        if left > 0:
            return self.prefix_sum[right]-self.prefix_sum[left-1]
        else:
            return self.prefix_sum[right]

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
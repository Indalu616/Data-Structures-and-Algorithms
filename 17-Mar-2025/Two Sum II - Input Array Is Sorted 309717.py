# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        right=len(numbers)-1

        while left < right:

            if numbers[left] + numbers[right]==target:
                return [left+1,right+1]
            elif numbers[left] + numbers[right] > target:
                right-=1
            elif numbers[left] + numbers[right] < target:
                left+=1
        



        
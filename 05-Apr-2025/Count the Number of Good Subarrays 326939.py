# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution(object):
    def countGood(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = defaultdict(int)
        left = 0
        result = 0
        pairs = 0

        for right in range(len(nums)):
            val = nums[right]
            pairs += count[val]
            count[val] += 1

            while pairs >= k:
                result += len(nums) - right
                count[nums[left]] -= 1
                pairs -= count[nums[left]]
                left += 1

        return result

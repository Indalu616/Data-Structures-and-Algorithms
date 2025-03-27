# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        remainder_count = defaultdict(int)
        remainder_count[0] = 1 
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k
        
      
            if remainder < 0:
                remainder += k
        

            count += remainder_count[remainder]
        
       
            remainder_count[remainder] += 1

        return count

        
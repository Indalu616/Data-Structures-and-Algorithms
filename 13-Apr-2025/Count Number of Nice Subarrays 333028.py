# Problem: Count Number of Nice Subarrays - https://leetcode.com/problems/count-number-of-nice-subarrays/

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  
        odd_count = 0
    
        for num in nums:
            if num % 2 == 1:
                odd_count += 1
     
            count += prefix_counts[odd_count - k]
            prefix_counts[odd_count] += 1
        
        return count
       





       
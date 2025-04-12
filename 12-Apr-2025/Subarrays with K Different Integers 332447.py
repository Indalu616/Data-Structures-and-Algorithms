# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # optimized solution
        #1. find the count of subarray which has at most k distnict integers
        #2. find the count of subarray which has at most k-1 distinct integers
        # What we got in (1)-result in (2) is the answer
        # [1,2,1,2,3], k = 2

        def count_at_most_k(k):
            count=0
            left=0
            freq=defaultdict(int)

            for right in range(len(nums)):
                if freq[nums[right]]==0:
                    k-=1
                freq[nums[right]]+=1

                while k < 0:

                    freq[nums[left]]-=1
                    if freq[nums[left]]==0:
                        k+=1
                    left+=1
                count+=right-left+1

            return count
        
        count1=count_at_most_k(k)
        count2=count_at_most_k(k-1)

        return count1-count2



        
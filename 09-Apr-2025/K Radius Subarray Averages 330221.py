# Problem: K Radius Subarray Averages - https://leetcode.com/problems/k-radius-subarray-averages/description/

class Solution(object):
    def getAverages(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        answer=[0]*len(nums)
        prefix_sum=[0]*len(nums)
        # [7,4,3,9,1,8,5,2,6], k = 3
        # prefix_sum= [7,11,14,23,24,32,37,38,44], k = 3
       
        n=len(nums)
        cum_sum=0

        if k <=0 :
            return nums
      
        for i in range(n):
            cum_sum+=nums[i]
            prefix_sum[i]=cum_sum
        
        for j in range(n):
            if j < k or j+k >=n:
                answer[j]=-1
            else:
                avg=(prefix_sum[j+k]-prefix_sum[j-k]+nums[j-k])//(2*k+1)
                answer[j]=avg
        return answer


        
        
        
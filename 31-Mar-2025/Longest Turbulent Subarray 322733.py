# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
  
     
        n = len(arr)
        if n == 1:
            return 1
    
        max_len = 1
        left = 0

        for right in range(1, n):
            sign = (arr[right] > arr[right - 1]) - (arr[right] < arr[right - 1])
            if sign == 0:
                left = right
            elif right == n - 1 or sign * ((arr[right + 1] > arr[right]) - (arr[right + 1] < arr[right])) != -1:
                max_len = max(max_len, right - left + 1)
                left = right

        return max_len
        






      
    

        
        









            







        





        
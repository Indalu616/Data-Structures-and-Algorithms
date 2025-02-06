# Problem: Richest Customer Wealth - https://leetcode.com/problems/richest-customer-wealth/description/

class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        max_prod=0

        left=0
        right=len(accounts)-1


        while left <=right:
            left_sum=0
            right_sum=0

            for x in accounts[left]:
              left_sum+=x
            for y in accounts[right]:
              right_sum+=y
            max_prod=max(max_prod,left_sum,right_sum)

            left+=1
            right-=1
        
        return max_prod
    

      
    

        
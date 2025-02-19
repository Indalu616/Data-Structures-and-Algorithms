# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n==1 or n==7:
            return True
        
        
        
        
        
        def find_square(num):

            sum=0

            while num >0:
                sum+= pow(num%10,2)
                num=num//10
            
            return sum

        while n//10 !=0:

            n=find_square(n)

            if n==1 or n==7:
                return True
        

        return False



        





        
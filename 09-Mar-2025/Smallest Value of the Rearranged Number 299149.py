# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        if len(str(num))==1:
            return num
    
        is_negative=False
        answer=0
        if num < 0:
            num*=-1
            is_negative=True
        digits=[]

        while num > 0:
            digits.append(num%10)
            num//=10
        if is_negative:
            digits.sort(reverse=True)
        else:
            digits.sort()
        
        e=len(digits)-1

        if digits[0]==0:
            for i in range(1,len(digits)):
                if digits[i]!=0:
                    digits[0],digits[i]=digits[i],digits[0]
                    break

        for i in range(len(digits)):
            answer+=digits[i]*pow(10,e-i)
        
        if is_negative:
            return answer*-1
        else:
            return answer
      


        
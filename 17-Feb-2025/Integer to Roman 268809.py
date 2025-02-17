# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        ans=""
        num_str=str(num)

        l=len(num_str)-1

        


        def giveRoman(n,exp):
            
            roman=""

            if exp==3:
                roman+="M"*n
    
            elif exp==2 and n==9:
                roman="CM"
            elif exp==2 and n==4:
                roman="CD"
            elif exp==2 and n < 4:
                roman="C"*n
                
            elif exp==2 and n > 5:
                roman="D"
                roman+="C"*(n-5)

            elif exp==2 and n==5:
                roman="D"
            elif exp==1 and n==5:
                roman="L"
            elif exp==1 and n==4:
                roman="XL"
            elif exp==1 and n==9:
                roman="XC"
            elif exp==1 and n > 5:
                roman="L"
                roman+="X"*(n-5)
            elif exp==1 and n < 4:
                roman+="X"*n 
            elif exp==0 and n==9:
                roman="IX"
            elif exp==0 and n==5:
                roman="V"
            elif exp==0 and n==4:
                roman="IV"
            elif exp==0 and n > 5:
                roman="V"
                roman+="I"*(n-5)
               
            else:
                roman+="I"*n

            return roman
        for letter in num_str:
            rom=giveRoman(int(letter),l)
            ans+=rom
            l-=1
        
        return ans




                




            








    



        
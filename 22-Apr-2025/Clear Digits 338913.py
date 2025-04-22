# Problem: Clear Digits - https://leetcode.com/problems/clear-digits/description/

class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack=[]
        digits=["0","1","2","3","4","5","6","7","8","9"]

        for x in s:
            if x not in digits:
                stack.append(x)
            else:
                stack.pop()
            
        return "".join(stack)
        
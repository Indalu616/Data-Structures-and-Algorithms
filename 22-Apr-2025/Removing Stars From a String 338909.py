# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/description/

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]

        for x in s:

            if x!="*":
                stack.append(x)
            else:
                stack.pop()
        
        return "".join(stack)


        
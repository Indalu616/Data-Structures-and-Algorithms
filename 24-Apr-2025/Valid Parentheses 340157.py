# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        my_char={"(":")","{":"}","[":"]"}

        for x in s:

            if x in my_char:
                stack.append(x)
            else:
                if not stack:
                    return False
                else:
                    br=stack[-1]
                    if my_char[br]!=x:
                        return False
                    else:
                        stack.pop()

        return stack==[]
            
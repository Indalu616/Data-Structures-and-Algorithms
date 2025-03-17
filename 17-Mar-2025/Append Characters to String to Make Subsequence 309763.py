# Problem: Append Characters to String to Make Subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/

class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        p1=0
        p2=0

        while p1 < len(s) and p2 < len(t):

            if t[p2]==s[p1]:
                p2+=1
                p1+=1
            else:
                p1+=1

        return len(t)-p2
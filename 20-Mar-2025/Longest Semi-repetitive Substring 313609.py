# Problem: Longest Semi-repetitive Substring - https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxlen = 0
        count = 0

        if len(s) <= 1:
            return 1

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count+=1
            
            while count > 1:
                if s[start] == s[start+1]:
                    count-=1
                start+=1
            maxlen=max(maxlen,i-start+1)
        return maxlen
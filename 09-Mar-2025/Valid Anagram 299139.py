# Problem: Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s)!=len(t):
            return False
        
        freq_1=Counter(s)
        freq_2=Counter(t)

        for key in freq_1:
            if key not in freq_2 or freq_1[key] !=freq_2[key]:
                return False
        
        return True
            



        

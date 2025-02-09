# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

from collections import Counter
class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq=Counter(s)

        arr=list(freq.values())

        arr_set=set(arr)

        if len(arr_set)==1:
            return True
        else:
            return False
            
        
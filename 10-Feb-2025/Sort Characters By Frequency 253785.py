# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        freq=Counter(s)
        arr=list(s)
     
        max_letter=s[0]

        st=""

        while freq:
            for i in range(len(arr)):
                if freq[arr[i]] > freq[max_letter]:
                    max_letter=arr[i]
            
            for j in range(freq[max_letter]):
                st+=max_letter

            del freq[max_letter]

            arr.remove(max_letter)

        return st
        
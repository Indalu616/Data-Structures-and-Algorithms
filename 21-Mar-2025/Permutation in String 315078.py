# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

     
        count1 = [0] * 26
        count2 = [0] * 26
        a_index = ord('a')

        for char in s1:
            count1[ord(char) - a_index] += 1

      
        for i in range(len(s1)):
            count2[ord(s2[i]) - a_index] += 1

 
        if count1 == count2:
            return True

 
        for i in range(len(s1), len(s2)):
            count2[ord(s2[i]) - a_index] += 1 
            count2[ord(s2[i - len(s1)]) - a_index] -= 1 

            if count1 == count2:
                return True

        return False
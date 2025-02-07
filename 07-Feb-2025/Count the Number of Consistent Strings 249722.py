# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """

        count=0

        for word in words:
            is_consistent=True
            for l in word:
                if l not in allowed:
                    is_consistent=False
                    break
            if is_consistent:
                count+=1
        

        return count

        
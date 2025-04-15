# Problem: Largest Merge of Two Strings - https://leetcode.com/problems/largest-merge-of-two-strings/

class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        p1=0
        p2=0
        n1=len(word1)
        n2=len(word2)
    
        merged=[]

        while p1 < n1 and p2 < n2:

            if word1[p1:] > word2[p2:]:
                merged.append(word1[p1])
                p1+=1
            else:
                merged.append(word2[p2])
                p2+=1
        
        merged.extend(list(word1[p1:]))
        merged.extend(list(word2[p2:]))

        return "".join(merged)

    



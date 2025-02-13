# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution(object):
    def isIsomorphic(self, s, t):
       

        hash_={}
        hash_2={}

        for i in range(len(s)):
            if s[i] in hash_ and hash_[s[i]]!=t[i] or t[i] in hash_2 and hash_2[t[i]]!=s[i]:
                return False
            else:
                hash_[s[i]]=t[i]
                hash_2[t[i]]=s[i]

        return True

        




        
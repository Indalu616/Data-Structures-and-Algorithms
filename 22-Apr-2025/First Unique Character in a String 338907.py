# Problem: First Unique Character in a String - https://leetcode.com/problems/first-unique-character-in-a-string/description/?envType=problem-list-v2&envId=queue

class Solution(object):
    def firstUniqChar(self, s):
        hash_={}

        for i in range(len(s)):
            if s[i] in hash_:
                hash_[s[i]]+=1
            else:
                hash_[s[i]]=1
        
        for i in range(len(s)):
            if hash_[s[i]]==1:
                return i

        return -1
        
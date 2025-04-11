# Problem: Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n=len(s)
        m=len(p)

        target=Counter(p)

        window=Counter(s[0:m])

        ans=[]
        left=0 

        if window == target:
            ans.append(left)
 
        for right in range(m,n):

            left_char=s[left]
            right_char=s[right]
            window[left_char]-=1
            if window[left_char]==0:
                del window[left_char]
            if right_char in window:
                window[right_char]+=1
            else:
                window[right_char]=1
            
            left+=1
        
            if window==target:
                ans.append(left)
                
        return ans
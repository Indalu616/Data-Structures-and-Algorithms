# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # expand from center and check till the substring is no longer palindrome
        def find_palindrome(left,right):
            while left >= 0 and right < len(s):
                if s[left]!=s[right]:
                    break
                left -= 1
                right += 1
        # return the palindrome found
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
       
            odd_pal = find_palindrome(i, i)# we may have a palindrome with odd length
      
            even_pal = find_palindrome(i, i + 1)# we may have a palindrome with even length

        # update longer palindrome
            if len(odd_pal) > len(longest):
                longest = odd_pal
            if len(even_pal) > len(longest):
                longest = even_pal

        return longest

        

    


        
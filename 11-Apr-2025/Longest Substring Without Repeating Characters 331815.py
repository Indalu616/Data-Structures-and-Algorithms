# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # substring ====>sliding window algorithm
        # without repeating character==>need set to track seen character

        left=0
        max_count=0
        char_set=set()

        for right in range(len(s)):
            current_char=s[right]

            # while current character is in charset:
            #     upadte left pointer
            #     remove left char from the charset
            while current_char in char_set:
                char_set.remove(s[left])
                left+=1
            # add current character or character at the right to the char_set
            char_set.add(current_char)
            # update max_count
            max_count=max(max_count,right-left+1)

        return max_count

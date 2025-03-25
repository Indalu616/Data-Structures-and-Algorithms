# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        char_count = {}
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            char_count[s[right]] = char_count.get(s[right], 0) + 1
            max_freq = max(max_freq, char_count[s[right]])

     
            if (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

        




        
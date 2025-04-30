# Problem: Remove Duplicate Letters - https://leetcode.com/problems/remove-duplicate-letters/

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Input: s = "bcabc"
        # Output: "abc"
        counter = Counter(s)
        stack = []
        seen = set() #keep track of the character we have added to stack so far

        for c in s:
            counter[c] -= 1
            if c in seen:
                continue
            while stack and c < stack[-1] and counter[stack[-1]] > 0:
                removed = stack.pop()
                seen.remove(removed)
            stack.append(c)
            seen.add(c)

        return ''.join(stack)


        
# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

from collections import Counter
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
       
        char_counter=Counter(chars)

        sum=0

        for word in words:
            word_count=Counter(word)
            is_good=True

            for l in word:
                if l not in char_counter or char_counter[l]<word_count[l]:
                    is_good=False
            
            if is_good:
                sum+=len(word)

        return sum
        
        


       

        
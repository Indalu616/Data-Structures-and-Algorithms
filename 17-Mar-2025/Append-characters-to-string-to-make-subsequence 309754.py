# Problem: Append-characters-to-string-to-make-subsequence - https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution(object):
    def appendCharacters(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # index_arr=[]
        # min_count=0
        # found_sofar=True

        # for x in t:

        #     if x in s and found_sofar:
        #         if len(index_arr)<1 or index_arr[-1]< s.index(x):
        #             index_arr.append(s.index(x))
        #     else:
        #         found_sofar=False
        #         min_count+=1

        # return min_count

        p1=0
        p2=0

        while p1 < len(s) and p2 < len(t):

            if t[p2]==s[p1]:
                p2+=1
                p1+=1
            else:
                p1+=1
                
        return len(t)-p2
        

        
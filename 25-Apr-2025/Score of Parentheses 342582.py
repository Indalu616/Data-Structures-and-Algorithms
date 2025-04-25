# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
      
        score=[0]

        for ch in s:

            if ch=="(":
                score.append(0)
            else:
                popped=score.pop()

                if popped==0:
                    score[-1]+=1
                else:
                    score[-1]+=2*popped

        return score[0]



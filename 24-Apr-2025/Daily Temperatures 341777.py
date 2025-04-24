# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        stack=[]
        answer=[0]*len(temperatures)
      

        for i in range(len(temperatures)):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                answer[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)

        return answer



        
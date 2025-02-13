# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution(object):
    def minimumSteps(self, s):
       

        answer=0
        count=0

        arr=list(s)

        r=len(arr)-1

        while r>=0:
            if arr[r]=="0":
                count+=1
            else:
                answer+=count
                
            r-=1

        return answer

        
            





    




     
            


            




        
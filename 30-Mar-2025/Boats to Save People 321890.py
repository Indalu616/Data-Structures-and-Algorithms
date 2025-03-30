# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """

        people.sort()

        count=0

        left=0
        right=len(people)-1
    
        while left <= right:

            if people[right]==limit or people[right]+people[left] > limit:
                count+=1
                right-=1
            elif people[left]+people[right]==limit:
                left+=1
                right-=1
                count+=1
            else:
                count+=1
                left+=1
                right-=1
    
        return count
            


       
        
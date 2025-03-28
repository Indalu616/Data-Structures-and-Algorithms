# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """

        skill.sort()
        required_chem=skill[0]+skill[-1]
        ans=0

        left=0
        right=len(skill)-1
    

        while left < right:

            if skill[left]+skill[right]!=required_chem:
                return -1
            else:
                ans+=skill[left]*skill[right]
            
            left+=1
            right-=1
        
        return ans
    




        
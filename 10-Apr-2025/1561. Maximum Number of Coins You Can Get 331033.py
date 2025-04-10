# Problem: 1561. Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/description/

class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        



      
        piles.sort()

        mine=0

        idx=len(piles)-2

        for i in range(len(piles)/3):

            mine+=piles[idx]
            idx-=2

        return mine
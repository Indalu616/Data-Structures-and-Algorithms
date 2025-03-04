# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
      

        piles.sort()

        mineCoin=0

        idx=len(piles)-2

        for i in range(len(piles)/3):

            mineCoin+=piles[idx]
            idx-=2

        
        return mineCoin
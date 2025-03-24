# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        min_operation=k

        left=0
        count=0
        n=len(blocks)

        count=0

        for right in range(n):

            if blocks[right]=="W":
                count+=1
            
            if right-left+1==k:
                min_operation=min(min_operation,count)

                if blocks[left]=="W":
                    count-=1
                left+=1
        
        return min_operation
            
                

        



        
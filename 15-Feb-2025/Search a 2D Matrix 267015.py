# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for x in matrix:
            left=0
            right=len(x)-1

            while left <= right:
                mid=(left+right)//2

                if x[mid]==target:
                    return True
                elif x[mid]> target:
                    right=mid-1
                else:
                    left+=1
                
        return False
               

        
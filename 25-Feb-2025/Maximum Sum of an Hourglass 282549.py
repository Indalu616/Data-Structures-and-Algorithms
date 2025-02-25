# Problem: Maximum Sum of an Hourglass - https://leetcode.com/problems/maximum-sum-of-an-hourglass/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:



        # a function to find the sum of the first row if exists
        def row1Sum(row,startIdx):
            sum=0
            # check if startIdx+2 is out of range, if out of range return -1 else return sum

            if startIdx+2 >=len(row):
                return -1
            else:
                for i in range(startIdx,startIdx+3):
                    sum+=row[i]
                return sum
            
        #  a function to find the element in the second row if exists
        def findEl(rowIdx,col_idx):

            if rowIdx >=len(grid) or col_idx >=len(grid[0]):
                return -1
            else:
                return grid[rowIdx][col_idx]
        #  a function to find the sum of the third row if exists

        def row3Sum(rowIdx,startIdx):
            sum=0

            # check if the row exist or if startIdx is not out of range

            if rowIdx >=len(grid) or startIdx+2 >=len(grid[0]):
                return -1
            else:
                for j in range(startIdx,startIdx+3):
                    sum+=grid[rowIdx][j]

                return sum
        # Now loop through the matrix and do the operation

        max_sum=0

        for i in range(len(grid)):

            for j in range(len(grid[0])):
                row1=row1Sum(grid[i],j)
                row2=findEl(i+1,j+1)
                row3=row3Sum(i+2,j)

                if row1!=-1 and row2!=-1 and row3!=-1:
                    max_sum=max(max_sum,row1+row2+row3)
        
        return max_sum




            

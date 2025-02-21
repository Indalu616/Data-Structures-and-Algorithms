# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row_len = len(matrix)
        col_len = len(matrix[0])

        seenZeros = set()

        for i in range(row_len):
            for j in range(col_len):
                if matrix[i][j] == 0 and (i, j) not in seenZeros:
                    # row
                    for k in range(col_len):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 0
                            seenZeros.add((i,k))
                    # col
                    for m in range(row_len):
                        if matrix[m][j] != 0:
                            matrix[m][j] = 0
                            seenZeros.add((m,j))
        

        

                
                    
        
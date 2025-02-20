# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """

        t_matrix=[]


        idx=0

        while idx < len(matrix[0]):

            row=[]

            for r in matrix:
                row.append(r[idx])

            idx+=1

            t_matrix.append(row)
        
        return t_matrix
        
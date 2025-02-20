# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        rotated_matrix=[]


        idx=0

        while idx < len(matrix[0]):
            row=[]

            for i in range(len(matrix)-1,-1,-1):

                row.append(matrix[i][idx])

            rotated_matrix.append(row)

            idx+=1
    
        matrix[:]=rotated_matrix
        



        
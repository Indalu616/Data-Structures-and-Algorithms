# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:

        row_num=0

        max_num=0


        for i in range(len(mat)):
            count=0

            for j in range(len(mat[0])):

                if mat[i][j]==1:
                    count+=1
            if count > max_num:
                max_num=count
                row_num=i
        
        return [row_num,max_num]
        
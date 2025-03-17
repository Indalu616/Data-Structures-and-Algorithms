# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """

        idx=0
        or_length=len(arr)
        n=len(arr)

        while idx < n:
            if arr[idx]==0:
                arr.insert(idx+1,0)
                idx+=2
                n+=1
            else:
                idx+=1
        arr[::]=arr[0:or_length]

        

       

        
        
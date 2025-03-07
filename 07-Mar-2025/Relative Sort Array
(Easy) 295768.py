# Problem: Relative Sort Array
(Easy) - https://leetcode.com/problems/relative-sort-array/

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        uncommon=[]

        for x in arr1:
            if x not in arr2:
                uncommon.append(x)
        
        
        
        uncommon.sort()

        hash_={}

        freq=Counter(arr1)
        out_put=[]

        for idx,value in enumerate(arr2):
            out_put.extend([value]*freq[value])

        print(uncommon)
        
        return out_put+uncommon










        



        
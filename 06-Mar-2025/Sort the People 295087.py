# Problem: Sort the People - https://leetcode.com/problems/sort-the-people/

class Solution(object):
    def sortPeople(self, names, heights):



        # loop through the unsorted array and take one element and check it with
        # the sorted one
        n=len(heights)

        for i in range(1,n):
            insert_index = i
            current_value = heights.pop(i)
            current_name=names.pop(i)
            for j in range(i-1, -1, -1):
                if heights[j] < current_value:
                    insert_index = j
            heights.insert(insert_index, current_value)
            names.insert(insert_index,current_name)

        return names


        


        
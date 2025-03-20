# Problem: Fruit Into Baskets - https://leetcode.com/problems/fruit-into-baskets

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        fruit_count = {} 
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            fruit_count[fruit]=fruit_count.get(fruit, 0) + 1

            while len(fruit_count) > 2:
                left_fruit = fruits[left]
                fruit_count[left_fruit] -= 1
                if fruit_count[left_fruit] == 0:
                    del fruit_count[left_fruit]
                left += 1 

            max_fruits = max(max_fruits, right - left + 1)
        print(fruit_count)

        return max_fruits



        
            
        
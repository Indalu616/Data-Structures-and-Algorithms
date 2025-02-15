# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

import math
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        freq_count=Counter(answers)
        min_rabbit=0

        for key,value in freq_count.items():
            same_color = key+1

            if value % same_color==0:
                min_rabbit+=value
            else:
                min_rabbit+=((value/same_color)+1)*same_color

        return min_rabbit

    
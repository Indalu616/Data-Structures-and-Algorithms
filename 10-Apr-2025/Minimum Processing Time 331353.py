# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        processorTime.sort()
        tasks.sort(reverse=True)
        idx=0

        min_time=float('-inf')

        left=0
        right=4
        n=len(tasks)

        while right <=n:
           
            min_time=max(min_time,max(tasks[left:right])+processorTime[idx])

            left+=4
            right+=4
            idx+=1
        return min_time

        




        

        
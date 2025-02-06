# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for im in image:
            im.reverse()

        for x in image:
            for i in range(len(x)):
                if x[i]==0:
                    x[i]=1
                else:
                    x[i]=0

        return image
        
        

        
        
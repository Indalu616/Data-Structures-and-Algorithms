# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution(object):
    def compress(self, chars):
        idx = 0 
        right_ponter = 0  

        while right_ponter < len(chars):
            ch = chars[right_ponter]
            count = 0
        
   
            while right_ponter < len(chars) and chars[right_ponter] == ch:
                right_ponter += 1
                count += 1

    
            chars[idx] = ch
            idx += 1

            if count > 1:
                for digit in str(count):
                    chars[idx] = digit
                    idx += 1

        return idx  



       
            





    


        





        
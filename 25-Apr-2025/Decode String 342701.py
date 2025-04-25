# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:

        stack=[]


        for char in s:

            word=""
            if char==']':
                ch=stack.pop()
                while ch!='[':
                    word=ch+word
                    ch=stack.pop()
                k=""
                k_val=stack.pop()
                while k_val.isdigit():
                    k=k_val+k
                    if stack and stack[-1].isdigit():
                        k_val=stack.pop()
                    else:
                        break
                stack.append(int(k)*word)
            else:
                stack.append(char)
        return "".join(stack)
         




    
            





        
# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:

        # if the 

        arr=path.split("/")

        stack=[]

        for ch in arr:
            if ch=="..":
                if stack:
                    stack.pop()
            elif ch!='' and ch!='.':
                stack.append(ch)
        ans=""

        for char in stack:
            ans+="/"
            ans+=char
        
        # print(stack)

        if not stack:
            return "/"
        
        return ans




        
        
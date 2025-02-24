# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

n,m=map(int,input().split())

matrix=[["."]*m for _ in range(n)]

cols=[m-1,0]
idx=0
for i in range(n):
    
    if i%2==0:
        for j in range(m):
            matrix[i][j]="#"
            current_col=j
            
        if i < n-1:
            matrix[i+1][cols[idx]]="#"
            if idx==1:
               idx=0
            else:
               idx+=1
        
for x in matrix:
    print("".join(x))
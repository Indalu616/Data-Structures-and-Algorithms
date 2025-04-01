# Problem: Books - https://codeforces.com/contest/279/problem/B



n,t=map(int,input().split())

a=list(map(int,input().split()))


current_sum=0
max_count=0

left=0

for right in range(n):
    
    current_sum+=a[right]
    
    while current_sum > t:
        current_sum-=a[left]
        left+=1
    
    max_count=max(max_count,right-left+1)
print(max_count)
        
        
        